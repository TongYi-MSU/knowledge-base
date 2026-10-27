# 🧠 Personal Knowledge Base｜个人知识库

将 ChatGPT 讨论中值得长期保存的结论整理为可浏览、可检索、可修订的 Markdown 知识资产。本仓库不是完整聊天记录备份。

## 🗂️ 知识目录

**目录是上下级关系。** 如 `mathematics/numerical-analysis/newton-method.md` 表示“数学 → 数值分析 → 牛顿法笔记”。以下只展示已建立的类别，后续可按需要动态增设。

| 一级目录 | 已有子分类 | 说明 |
|---|---|---|
| [数学](mathematics/README.md) | [数值分析](mathematics/numerical-analysis/README.md)、[微分方程](mathematics/differential-equations/README.md)、[线性代数](mathematics/linear-algebra/README.md) | 证明、公式、算法 |
| [计算机科学](computer-science/README.md) | 按需建立 | 算法、AI、操作系统 |
| [工程技术](engineering/README.md) | [电子工程](engineering/electronics/README.md)、[机械工程](engineering/mechanical/README.md)、[材料工程](engineering/materials/README.md) | PCB、电路、机械、材料 |
| [物理](physics/README.md) | 按需建立 | 概念、理论、实验 |
| [语言](languages/README.md) | 按需建立 | 俄语、土耳其语等 |
| [音乐](music/README.md) | [乐器](music/instruments/README.md)、[音乐作品](music/works/README.md) | 吉他、Bağlama 等 |
| [影视](film-and-tv/README.md) | [电影](film-and-tv/movies/README.md)、[电视剧](film-and-tv/television/README.md)、[动画](film-and-tv/animation/README.md) | 作品、鉴赏、解析 |
| [图片识别](image-identification/README.md) | [旅游目的地](image-identification/travel-destinations/README.md)、[产品](image-identification/products/README.md)、[食物](image-identification/food/README.md) | 图片识别结果独立归档 |
| [旅行](travel/README.md) | 按需建立 | 国家、城市、攻略 |
| [历史文化](history-and-culture/README.md) | [饮食文化](history-and-culture/cuisine/README.md)、[科学技术史](history-and-culture/history-of-science/README.md)、[人物](history-and-culture/people/README.md)、[文化传统](history-and-culture/traditions/README.md) | 历史、诗人、科技史与各地文化 |
| [生活](life/README.md) | 按需建立 | 实用知识 |

## ✍️ 归档工作流

用户说 **「归档本次讨论」** 后，归档助手应：

1. **实际读取 GitHub 最新版**本文件、[RULES.md](RULES.md)和 [AGENTS.md](AGENTS.md)，检查真实目录。
2. 检索已有相关知识：优先更新旧笔记，避免重复。
3. 选择正确的多级分类；新类别按需创建目录及目录导航 `README.md`。
4. 按[模板](templates/knowledge-note.md)或相应专项模板整理结论、推导、来源、不确定性。
5. 对具象主题核验并精选**可直接显示的代表图片**，尽可能在笔记标题附近嵌入，明确区分用户原图与搜索所得参考图。
6. 更新父级索引，运行或对照[结构校验](scripts/validate.py)，提交到 GitHub。
7. 回报实际文件链接、**图片保存/显示状态**与验证结果；无法访问或提交时如实说明。

**只在用户明确要求时归档**。普通新对话不会自动读取本仓库；可使用[ChatGPT Project 指令](docs/CHATGPT_PROJECT_INSTRUCTIONS.md)，但依然需要真正访问 GitHub。

## 🌿 发散性对话如何归档

**按主题归档，不按对话归档。** 同一聊天中，多个独立知识主题可以产生多篇笔记；围绕同一个概念的公式、例子和相关问答应合并，不机械按消息拆分。前后不连续的同主题内容要归入同一组；低价值插话可以略过。

**综合专题是可选的。** 多个独立主题如果共同回答一个核心研究问题，可以额外建立一篇综合专题，保留论证脉络并链接独立笔记；不复制各篇全文，也不专设按聊天日期收集的目录。

归档流程应对每个主题分别查重、更新或新建，**尽量将本次所有笔记与目录索引一次 Git Commit 提交**，避免提交中途出现断链；结束后生成逐主题报告（新增／更新／合并／略过）及实际 CI 状态。

具体要求见 [RULES.md 的多主题归档协议](RULES.md#h-多主题对话智能归档协议)。

## 📐 根规则

- **动态目录树**：优先已有分类；必要时自动创建一级、二级、三级分类；通常最多三级，禁止为每篇笔记单独套文件夹。
- **图片识别专用入口**：以用户提供的图片为研究对象时，优先放在 `image-identification/`，二级按旅游目的地、产品、食物、动物、植物、艺术品等分类，再向下细分国家或种类。
- **旅行与图片识别分开**：例如照片辨认某建筑放 `image-identification/travel-destinations/`；对该地点的旅行攻略另放 `travel/` 并互链。
- **一对话可多主题**：先扫描、聚类，再按知识主题拆分或合并，必要时建立综合专题。
- **一主题一主位置**：跨学科用 Markdown 相对链接与标签，不复制相同文章。
- **内容准确**：区分事实、观察、推断、个人观点及待核实结论；时效性信息注明地域和核验日期。
- **保留重要细节**：数学/工程笔记必须保留必要公式、条件、证明或技术参数；不要逐条粘贴聊天记录。
- **保存原始素材**：用户请求归档的图片、诗歌、歌词、文本等资料，在取得原件时尽量按原始格式保存并与笔记关联；保留出处、版本和核验情况，不能获取时说明原因。
- **Wiki 可视化**：具象主题优先选择经过核验的图片搜索结果或原图，在笔记开头嵌入代表图，让 GitHub/Obsidian 打开后可以直观看到研究对象；本地图片优先，外链需保证是图片直链并记录来源，不用相似图冒充已识别原图。
- **隐私保护**：仓库保持 Private；不得自动保存密码、令牌和敏感个人信息。
- **统一元数据**：知识笔记使用 Markdown、英文小写连字符文件名与 YAML frontmatter；目录用 `README.md` 导航。
- **可信的验证**：GitHub Actions 检查文件结构和链接，不保证事实真实性或语义去重。

本文件为根规则；[RULES.md](RULES.md) 提供详细操作。发生冲突时以本文件的根规则为准。

## 🛠️ 项目文件

- [详细归档与分类规范](RULES.md)
- [AI 执行说明](AGENTS.md)
- [原始资料的保全规范](RULES.md#i-原始资料保全与溯源)
- [Wiki 图像搜索、核验与嵌入规范](RULES.md#j-图文并茂的-wiki-可视化归档)
- [普通笔记模板](templates/knowledge-note.md)
- [图片识别模板](templates/image-identification-note.md)
- [旅行目的地模板](templates/travel-destination-note.md)
- [影视模板](templates/film-tv-note.md)
- [ChatGPT Project 指令](docs/CHATGPT_PROJECT_INSTRUCTIONS.md)

本地检查：`python3 scripts/validate.py`；推送和 Pull Request 也会触发 CI 检查。
