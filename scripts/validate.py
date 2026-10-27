#!/usr/bin/env python3
"""Validate Markdown structure, paths and links; factual accuracy requires separate review."""
from datetime import date
from pathlib import Path
from urllib.parse import unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
RESERVED = {'.github', '.git', '.obsidian', 'docs', 'templates', 'scripts'}
REQUIRED = {'title', 'created', 'updated', 'tags', 'type'}
TYPES = {'knowledge', 'image-identification', 'travel', 'film-tv'}
SLUG = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
LINK = re.compile(r'!?\[[^\]\n]*\]\((?:<([^>]+)>|([^\)]+))\)')  # also validates local Markdown images
errors = []

def issue(path, detail):
    errors.append(f"{path.relative_to(ROOT)}: {detail}")

def check_links(path, data):
    # Markdown examples inside code fences or inline code are not real links.
    data = re.sub(r'(?ms)^```[^\n]*\n.*?^```[ \t]*
        target = (match.group(1) or match.group(2)).strip().split(' "', 1)[0]
        if not target or target.startswith(('#', 'https://', 'http://', 'mailto:', 'data:')):
            continue
        target = unquote(target.split('#', 1)[0].split('?', 1)[0])
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.is_relative_to(ROOT.resolve()):
            issue(path, f"link outside repository: {target}")
        elif not resolved.exists():
            issue(path, f"broken relative link: {target}")

def check_note(path, content):
    lines = content.splitlines()
    if not lines or lines[0].strip() != '---':
        issue(path, 'missing YAML frontmatter')
        return
    try:
        stop = lines.index('---', 1)
    except ValueError:
        issue(path, 'missing YAML closing delimiter')
        return
    meta = {}
    for line in lines[1:stop]:
        if not line.strip() or line.startswith('#'):
            continue
        matched = re.fullmatch(r'([a-z][a-z0-9_-]*):\s*(.*)', line)
        if not matched:
            issue(path, f"invalid YAML line: {line}")
            continue
        key, value = matched.groups()
        if key in meta:
            issue(path, f"duplicate field: {key}")
        meta[key] = value.strip()
    for key in sorted(REQUIRED - meta.keys()):
        issue(path, f"missing field: {key}")
    kind = meta.get('type', '')
    if kind not in TYPES:
        issue(path, f"invalid type: {kind}")
    rel = path.relative_to(ROOT)
    required_type = {'image-identification': 'image-identification', 'travel': 'travel', 'film-and-tv': 'film-tv'}.get(rel.parts[0])
    if required_type and kind != required_type:
        issue(path, f"expected type: {required_type}")
    for key in ('created', 'updated'):
        value = meta.get(key, '')
        if not DATE.fullmatch(value):
            issue(path, f"{key} must be YYYY-MM-DD")
        else:
            try:
                date.fromisoformat(value)
            except ValueError:
                issue(path, f"{key} invalid date")
    if DATE.fullmatch(meta.get('created', '')) and DATE.fullmatch(meta.get('updated', '')) and meta['updated'] < meta['created']:
        issue(path, 'updated precedes created')
    if not meta.get('title'):
        issue(path, 'missing title value')
    if not re.fullmatch(r'\[[^\[\]]*\]', meta.get('tags', '')):
        issue(path, 'tags must be an inline YAML list')
    body = '\n'.join(lines[stop + 1:])
    if not re.search(r'^#\s+\S', body, re.M):
        issue(path, 'missing # heading')
    headings = {
        'knowledge': ('## 一句话总结', '## 核心知识'),
        'image-identification': ('## 识别结论', '## 图片中的可见特征', '## 判断依据与不确定性'),
        'travel': ('## 一句话总结', '## 旅行实用信息'),
        'film-tv': ('## 作品信息', '## 一句话总结'),
    }
    for heading in headings.get(kind, ()):
        if not re.search('^' + re.escape(heading) + r'\s*$', body, re.M):
            issue(path, f"missing section: {heading}")
    if kind == 'image-identification' and meta.get('status') not in {'confirmed','probable','uncertain'}:
        issue(path, 'image records need status confirmed|probable|uncertain')

def main():
    for path in sorted(ROOT.rglob('*')):
        rel = path.relative_to(ROOT)
        if any(part in {'.git', '.obsidian', '__pycache__'} for part in rel.parts):
            continue
        if rel.parts[0] not in RESERVED and path.is_dir():
            if len(rel.parts) > 3:
                issue(path, 'directory depth exceeds three')
            for part in rel.parts:
                if not SLUG.fullmatch(part):
                    issue(path, f"invalid directory name: {part}")
            if not (path / 'README.md').is_file():
                issue(path, 'directory missing README.md navigation')
        if not path.is_file() or path.suffix != '.md':
            continue
        content = path.read_text(encoding='utf-8')
        check_links(path, content)
        if rel.parts[0] in RESERVED or path.name in {'README.md','RULES.md','AGENTS.md'}:
            continue
        if not SLUG.fullmatch(path.stem):
            issue(path, 'filename must be lowercase-kebab-case')
        check_note(path, content)
    if errors:
        print(f'FAIL ({len(errors)} issues)')
        for err in errors:
            print(' -', err)
        return 1
    print('PASS: Markdown links and local images, navigation, metadata, required sections')
    print('NOTE: CI cannot verify factual accuracy, duplicate meaning, or external image links.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
, '', data)
    data = re.sub(r'`+[^`\n]*`+', '', data)
    for match in LINK.finditer(data):
        target = (match.group(1) or match.group(2)).strip().split(' "', 1)[0]
        if not target or target.startswith(('#', 'https://', 'http://', 'mailto:', 'data:')):
            continue
        target = unquote(target.split('#', 1)[0].split('?', 1)[0])
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.is_relative_to(ROOT.resolve()):
            issue(path, f"link outside repository: {target}")
        elif not resolved.exists():
            issue(path, f"broken relative link: {target}")

def check_note(path, content):
    lines = content.splitlines()
    if not lines or lines[0].strip() != '---':
        issue(path, 'missing YAML frontmatter')
        return
    try:
        stop = lines.index('---', 1)
    except ValueError:
        issue(path, 'missing YAML closing delimiter')
        return
    meta = {}
    for line in lines[1:stop]:
        if not line.strip() or line.startswith('#'):
            continue
        matched = re.fullmatch(r'([a-z][a-z0-9_-]*):\s*(.*)', line)
        if not matched:
            issue(path, f"invalid YAML line: {line}")
            continue
        key, value = matched.groups()
        if key in meta:
            issue(path, f"duplicate field: {key}")
        meta[key] = value.strip()
    for key in sorted(REQUIRED - meta.keys()):
        issue(path, f"missing field: {key}")
    kind = meta.get('type', '')
    if kind not in TYPES:
        issue(path, f"invalid type: {kind}")
    rel = path.relative_to(ROOT)
    required_type = {'image-identification': 'image-identification', 'travel': 'travel', 'film-and-tv': 'film-tv'}.get(rel.parts[0])
    if required_type and kind != required_type:
        issue(path, f"expected type: {required_type}")
    for key in ('created', 'updated'):
        value = meta.get(key, '')
        if not DATE.fullmatch(value):
            issue(path, f"{key} must be YYYY-MM-DD")
        else:
            try:
                date.fromisoformat(value)
            except ValueError:
                issue(path, f"{key} invalid date")
    if DATE.fullmatch(meta.get('created', '')) and DATE.fullmatch(meta.get('updated', '')) and meta['updated'] < meta['created']:
        issue(path, 'updated precedes created')
    if not meta.get('title'):
        issue(path, 'missing title value')
    if not re.fullmatch(r'\[[^\[\]]*\]', meta.get('tags', '')):
        issue(path, 'tags must be an inline YAML list')
    body = '\n'.join(lines[stop + 1:])
    if not re.search(r'^#\s+\S', body, re.M):
        issue(path, 'missing # heading')
    headings = {
        'knowledge': ('## 一句话总结', '## 核心知识'),
        'image-identification': ('## 识别结论', '## 图片中的可见特征', '## 判断依据与不确定性'),
        'travel': ('## 一句话总结', '## 旅行实用信息'),
        'film-tv': ('## 作品信息', '## 一句话总结'),
    }
    for heading in headings.get(kind, ()):
        if not re.search('^' + re.escape(heading) + r'\s*$', body, re.M):
            issue(path, f"missing section: {heading}")
    if kind == 'image-identification' and meta.get('status') not in {'confirmed','probable','uncertain'}:
        issue(path, 'image records need status confirmed|probable|uncertain')

def main():
    for path in sorted(ROOT.rglob('*')):
        rel = path.relative_to(ROOT)
        if any(part in {'.git', '.obsidian', '__pycache__'} for part in rel.parts):
            continue
        if rel.parts[0] not in RESERVED and path.is_dir():
            if len(rel.parts) > 3:
                issue(path, 'directory depth exceeds three')
            for part in rel.parts:
                if not SLUG.fullmatch(part):
                    issue(path, f"invalid directory name: {part}")
            if not (path / 'README.md').is_file():
                issue(path, 'directory missing README.md navigation')
        if not path.is_file() or path.suffix != '.md':
            continue
        content = path.read_text(encoding='utf-8')
        check_links(path, content)
        if rel.parts[0] in RESERVED or path.name in {'README.md','RULES.md','AGENTS.md'}:
            continue
        if not SLUG.fullmatch(path.stem):
            issue(path, 'filename must be lowercase-kebab-case')
        check_note(path, content)
    if errors:
        print(f'FAIL ({len(errors)} issues)')
        for err in errors:
            print(' -', err)
        return 1
    print('PASS: Markdown links and local images, navigation, metadata, required sections')
    print('NOTE: CI cannot verify factual accuracy, duplicate meaning, or external image links.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
