# Spring数据库设计

## 一、	需求分析

当代大学生在宿舍食堂图书馆三点一线的生活中，普遍存在交际面局限在宿舍、日益感到孤独自闭的现象，基于大学生之间的交流与交友需求，我们开发了一个平台——Spring，为广大大学生提供一个交流、交友的平台。考虑到交友的安全性与趣味性，我们的平台主要有两部分功能区来保障用户的使用体验：以题会友、兴趣匹配。并附加了暗恋点赞、我的后花园等功能。

### （一）	以题会友

有言道：有趣的灵魂千万，你是不是我的菜。Spring平台秉承人人出题、人人答题、以题会友的理念，在出题答题的来往间为你找到读得懂你的那个人。每个人可以设置属于自己的一套题目，供别人查看和答题，也可以删除和修改自己的题目，每个人也可以回答别人的问题，叩开Ta的心门。出题人有权利给每个回答者打分，答题者也可以查看自己的分数。高的答题得分为你匹配对的人。

### （二）	兴趣匹配

有言道：萝卜白菜，各有所爱。共同的兴趣爱好意味着两人之间更多的话题，也意味着更高的匹配概率，Spring平台可以实现用户自主添加标签，个人主页显示标签，并通过标签筛选用户的功能，帮你找到与你兴趣相投，能陪你从诗词歌赋聊到人生哲学的那个Ta。

### （三）	附加功能

1)	暗恋点赞

面对喜欢的人不敢开口怎么办？暗恋点赞来帮你！Spring平台为暗恋的人提供万无一失的告白方式，在你暗恋的人的主页为他点赞，实现暗恋操作。你也可以在个人主页查看与你相互暗恋的人，不敢说出来，那就点赞吧。

2)	我的后花园

Spring平台也可以成为你的博客，与他人分享你生活的点滴，将你的奇思妙想发在你的后花园里，访客也可以对你的博文进行评论，共同交流、共同进步。

## 二、	概要设计

### （一）	Spring平台中的实体及其之间的关系
 
### （二）	建表并生成E-R图
 
### （三）	实体与关系之间的说明

1.	一个用户可以拥有多个兴趣标签，也可以很多用户共享一个兴趣标签

2.	一个用户可以发布很多博客，但是一个博客只能有一个博主

3.	每个用户可以对多个博客发表多个评论，一个博客也可以拥有来自多个用户的评论

4.	每个用户可以给多人进行暗恋点赞操作

5.	出题人和答题人都只有一个，每个人可以出多道题，也可以回答多道题

6.	出题人可以给多个回答他问题的用户评分

### （四）	建表过程中对效率的考量

1.	考虑到用户的id需要被很多表参照，所以把用户的id与注册功能和基础信息分开单独建表，查询的时候可以提高效率。

## 三、	小组分工

### （一）	组员共同完成的工作：

1)	确定选题——搭建在线答题交友平台Spring

2)	确定工具——Django + MySQL

3)	绘制数据库系统的E-R图

4)	决定数据库的逻辑结构和物理结构

### （二）	小组成员细化分工如下：

1)	操懿：负责答题功能的业务逻辑层的构建

2)	曾千涵：负责前端界面层的构建，辅助构建答题功能的业务逻辑层的构建

3)	娄立威：负责前端界面层的构建，使用文档的书写

4)	麻世钰：负责用户登录注册模块和撰写博客模块的业务逻辑层构建和前端界面层的构建

5)	许智彤：负责用户登录注册模块和撰写博客模块的业务逻辑层构建和前端界面层的构建
