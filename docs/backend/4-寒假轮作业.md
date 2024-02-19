# 4-寒假轮作业

- 知识点
- 推荐教程
- 多人作业
- 单人作业

## 知识点

1. RESTAPI
2. JWT鉴权
3. 参数校验
4. ORM
5. 工程化
6. 异常处理
7. 文件处理
8. 日志
9. 权限
10. 参数校验
11. 缓存
12. docker
13. 雪花算法

## 推荐教程

1. RESTAPI
2. JWT鉴权知识 https://learnku.com/articles/17883 
3. JWT用法 https://blog.csdn.net/yangbindxj/article/details/125344291 （这里用了Fastapi的例子，其实jwt库两个都可以用）
4. ORM 用Flask推荐flask-sqlalchemy，用Fastapi推荐sqlalchemy，flask-sqlalchemy可以通过paginate分页比较方便，sqlalchemy分页需要offset+limit
5. 蓝图（Flask）/APIRouter（Fastapi）看各自的文档还有网上资料
6. 通过异常处理器（@app.errorhandler/@app.exception_handler）捕获异常（参数错误/token错误），并把异常结果格式化为应该返回的格式 
7. 文件的上传，响应文件下载
8. 推荐使用logging日志工具打印运行时的日志
9. 在登陆后在token中添加用户的权限信息，对于需要token的接口在JWT解码时进行权限检验和进行拦截，Flask使用装饰器，FastApi可以选择依赖注入，或者使用中间件拦截
10. FastiApi可以使用自带的参数检验，Flask应该引入Flask-Restful，规范RestfulAPi，同时使用其带的参数检验功能[Flask-RESTful](http://www.pythondoc.com/Flask-RESTful/index.html)
11. 在框架中接入redis等进行缓存，读写很快，可以用于缓存验证码，以及一些经常读写的信息
12. 部署项目环境弄起来非常的难受，建议大家学习一下docker，使用docker将项目部署到服务器
13. 各种id可以使用雪花算法来生成，防止数据库自增id过程出错

## 多人作业

> 本轮为第一轮寒假轮考核。今年我们在正式考核前加入了预热环节。

### 目的

- 与前端同学合作，实现前后端对接，实现项目的真正落地
- 对Flask的掌握
- 熟悉开发流程与规范

### 任务

#### Warm Up：实现一个简单的Todolist对接

- 这一步旨在先熟悉一下前后端该如何合作与对接（后端写的接口，前端该如何调用，前端发送的数据，后端该如何接收），不需要写很复杂，页面简单，能实现基本的待办清单功能即可。
- 也可以在第三轮的作业上进行修改，补充对接逻辑。
- 这个部分**为期7天**。

#### 寒假轮考核：仿一个社区平台——稀土掘金

> 红线涂掉的就是不需要的

1. 首页

   ⽂章榜：按点击量降序

   最新：最新发布的⽂章

   写⽂章按钮：点击之后进入文章编辑界面

   带头像的下拉菜单：有“我的主页”这一项就行

   [![img](https://github.com/west2-online-reserve/collection-frontends/raw/main/img/4-%E5%AF%92%E5%81%87%E5%90%88%E4%BD%9C%E8%BD%AE/image.png)](https://github.com/west2-online-reserve/collection-frontends/blob/main/img/4-寒假合作轮/image.png)

   [![img](https://github.com/west2-online-reserve/collection-frontends/raw/main/img/4-%E5%AF%92%E5%81%87%E5%90%88%E4%BD%9C%E8%BD%AE/image-1.png)](https://github.com/west2-online-reserve/collection-frontends/blob/main/img/4-寒假合作轮/image-1.png)

2. 文章页

   内容展示：Markdown 解析与渲染

   点赞按钮：点赞收藏文章

   评论功能：普通⽂本评论就⾏，不⽤加表情/图⽚/链接等，要求带⼦评论

   [![img](https://github.com/west2-online-reserve/collection-frontends/raw/main/img/4-%E5%AF%92%E5%81%87%E5%90%88%E4%BD%9C%E8%BD%AE/image-2.png)](https://github.com/west2-online-reserve/collection-frontends/blob/main/img/4-寒假合作轮/image-2.png)

   [![img](https://github.com/west2-online-reserve/collection-frontends/raw/main/img/4-%E5%AF%92%E5%81%87%E5%90%88%E4%BD%9C%E8%BD%AE/image-3.png)](https://github.com/west2-online-reserve/collection-frontends/blob/main/img/4-寒假合作轮/image-3.png)

3. 我的主页

   个人简介

   我写的⽂章

   我点赞的⽂章

   进入设置页按钮

   [![img](https://github.com/west2-online-reserve/collection-frontends/raw/main/img/4-%E5%AF%92%E5%81%87%E5%90%88%E4%BD%9C%E8%BD%AE/image-4.png)](https://github.com/west2-online-reserve/collection-frontends/blob/main/img/4-寒假合作轮/image-4.png)

4. 设置页

   支持修改用户名

   支持修改密码

   支持修改头像

   [![img](https://github.com/west2-online-reserve/collection-frontends/raw/main/img/4-%E5%AF%92%E5%81%87%E5%90%88%E4%BD%9C%E8%BD%AE/image-5.png)](https://github.com/west2-online-reserve/collection-frontends/blob/main/img/4-寒假合作轮/image-5.png)

5. 写文章界面

   拥有文章标题

   支持Markdown编写，且支持实时预览

   发布按钮

   其他都不需要

   [![img](https://github.com/west2-online-reserve/collection-frontends/raw/main/img/4-%E5%AF%92%E5%81%87%E5%90%88%E4%BD%9C%E8%BD%AE/image-6.png)](https://github.com/west2-online-reserve/collection-frontends/blob/main/img/4-寒假合作轮/image-6.png)

### 多人作业要求

1. 跨域功能
2. 登录注册功能，对应密码应该进行密码哈希处理
3. 对登录和注册的值进行检验，在检验有误时返回错误
4. 登录后后端生成token并返回给前端，有些接口要对token的权限进行检验，不合法、没有权限或者过期返回错误
5. 使用ORM对数据进行操作
6. 有清晰的项目结构，通过蓝图（Flask）或者APIRouter（Fastapi）进行分组
7. 编写接口文档

### Bonus

> 这些内容和组队的前端同学讨论后，自行选择性完成

1. 除了可以写⽂章，还有草稿箱：暂存写到⼀半的⽂章
2. ⽀持⽂章⽬录功能（点击后可以跳转到同⼀⻚⾯的位置）
3. 允许多层嵌套评论（现有的⽹站⼤多数使⽤⼆级评论，没有做到真正的多级）
4. ⽀持搜索功能（模糊搜索）
5. 点赞使⽤缓存处理，不要求很难的逻辑

## 单人作业

### 目的

- 掌握HTTP协议和Web工作原理
- 掌握现代 HTTP 框架开发流程
- 掌握数据库的增删改查(CRUD)及基础的数据库表设计
- 入门简单的缓存引入和使用
- 入门简单的项目设计模式

### 背景

金三银四来了！FanOne 正在准备面试，由于过于卷，于是想放松一下看一下番剧，可惜她又没有`大会员`，FanOne现在很苦恼

### 任务清单

> 请你写一个**视频网站**（写 API 文档接口即可），让LWGG能在没有大会员的条件下开心的追番吧！

请遵照以下接口文档完成功能

https://apifox.com/apidoc/shared-dcb1a5ef-5c75-4a0e-9486-e3bd748379a0

你不必完成以上的全部功能，以下完成本次作业的最低要求（共计 17 个接口，已经非常少了）

| 模块名 | 最低需要完成的接口                           | 数量 |
| ------ | -------------------------------------------- | ---- |
| 用户   | 注册、登录、用户信息、上传头像               | 4    |
| 视频   | 投稿、发布列表、搜索视频、热门排行榜         | 4    |
| 互动   | 点赞操作、点赞列表、评论、评论列表、删除评论 | 5    |
| 社交   | 关注操作、关注列表、粉丝列表、好友列表       | 4    |

别看很多，中间我们还砍掉了以下内容

### 你不需要完成的内容

除了上面没列出的接口外，你还不需要完成这些

- 不需要考虑性能，只需要完成项目即可
- 不需要考虑设计模式/项目结构，只需要完成项目即可
- *不需要考虑其他七七八八的，只需要跑通接口即可*
- 互动模块：评论接口只要求完成对视频的点赞，即 comment_id 字段的功能不需要实现，**我们只需要你完成对视频的评论即可，不需要实现对评论进行评论**
- 互动模块：点赞操作只要求完成对视频的点赞，不需要处理对评论的点赞
- 视频模块：投稿接口不要求实现分片上传和分布式存储，你只需要做到可以正常接收文件，并保存到本地某个目录下即可
- 社交模块：不需要完成 WebSocket 部分

### 提醒你需要完成的内容

- 分页管理：如果参数带有 page_num 和 page_size，需要正确识别并进行分页
- 视频搜索：考察简单的 SQL，因此搜索条件需要全部满足
- 删除评论：不可删除其他人的评论
- 需要支持双 Token
- 为你的项目提供一份**项目结构图（目录树）**
- 完成**Docker部署**（编写Dockerfile并且利用这个文件成功部署你的项目，不要求传镜像到 hub 上）
- **请求和返回结构必须遵循接口文档**

### Bonus

- 实现全部接口的全部功能
- 对点赞操作引入 Redis 缓存
- 不使用文档中的**投稿**接口，改用自己设计接口，以实现视频的分片上传与存储
- 实现WebSocket 聊天功能

### 提示

- Apifox 里可以直接调试哦
- 请关注你项目的逻辑，尤其是社交部分
- 请注意你的数据库表设计，尤其是互动和社交部分
- 热门排行榜考察的是你的 Redis 引入和使用，只需要中间使用到了 Redis 就行（例如，用户请求一次后你将排行榜存在 redis，后续请求直接从 redis 获取数据，不考虑过深的逻辑）
- **下半年的全部作业，都会要求你在本次项目的基础上进行增添和修改**，请认真对待你的项目结构
- 这次作业会考察关系型数据库表的设计以及你的设计模式、项目结构规范，**如果你认为你以上几个可能写的不理想，建议提前实现剩余接口和不要求完成的内容**，下一次答辩后会要求你修改你项目中不合理的结构和表设计

不要过度关注CURD的内容，请将目标放在下面这些

- 项目架构是否合理
- 数据库设计是否合理
- 是否对新技术（如Redis）的使用相对合理
- 每一个接口的逻辑是否正确（例如，在上传视频时是否考虑到了用户是否登录？）
- 你的接口能否支撑住多人访问？
- 当你使用缓存后，是否能避免出现缓存穿透，缓存雪崩等情况？

### 具体要求

- 跨域功能
- 登录注册功能，对应密码应该进行密码哈希处理
- 对登录和注册的值进行检验，在检验有误时按照要求返回结果
- 登录后后端生成token并返回给前端，除登录注册外的所有接口都要对token进行检验，不合法或者过期按照要求返回结果
- 使用ORM对数据进行操作
- 分页搜索
- 有清晰的项目结构，分为user/video等模块，通过蓝图（Flask）或者APIRouter（Fastapi）进行分组
- 符合RESTAPI（不符合你好像也对接不上）
