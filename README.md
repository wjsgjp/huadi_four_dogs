# up video 需求分析

## 接口文档

### 1. 获取接口
**接口名称**：获取筛选视频信息  
**接口地址**：`/up/videos`  
**请求方式**：GET  

#### 请求参数
 
 | 参数名称          | 参数类型 | 是否必填 | 参数描述                          |
 |-------------------|----------|----------|-------------------------------|
 | `bid`             | string   | 否       | 视频ID                          |
 | `title`           | string   | 否       | 视频标题                          |
 | `pubdate_start`   | string   | 否       | 开始发布日期，格式为YYYY-MM-DD HH:MM:SS |
 | `pubdate_end`     | string   | 否       | 结束发布日期，格式为YYYY-MM-DD HH:MM:SS |
 | `duration_min`    | int      | 否       | 最小时长                          |
 | `duration_max`    | int      | 否       | 最长时长                          |
 | `view`            | boolean  | 否       | 是否按播放量排序   默认为TRUE            |
 | `like`            | boolean  | 否       | 是否按点赞量排序                      |
 | `coin`            | boolean  | 否       | 是否按投币量排序                      |
 | `share`           | boolean  | 否       | 是否按分享量排序                      |
 | `danmaku`         | boolean  | 否       | 是否按弹幕量排序                      |
 | `reply`           | boolean  | 否       | 是否按评论量排序                      |
 | `favorite`        | boolean  | 否       | 是否按收藏量排序                      |
 | `uname`           | string   | 否       | UP主名称                         |
 | `tags`            | string   | 否       | 视频标签                          |
 | `date_order_desc` | boolean  | 否       | 是否按发布日期降序排序                   |
| `date_order_asc`  | boolean  | 否       | 是否按发布日期升序排序                   |

#### 请求示例

```http
GET http://127.0.0.1:5000/up/videos?uname=edg&date_order_desc=true&duration_min=10&title=S11
```
#### 响应参数

| 参数名称   | 参数描述                     |
|------------|------------------------------|
| `bid`      | 视频ID                       |
| `pic`      | 封面图片URL                  |
| `title`    | 视频标题                     |
| `pubdate`  | 发布日期（Unix时间戳，毫秒） |
| `duration` | 视频时长（秒）               |
| `view`     | 播放量                       |
| `like`     | 点赞数                       |
| `coin`     | 硬币数                       |
| `share`    | 分享数                       |
| `danmaku`  | 弹幕数                       |
| `reply`    | 评论数                       |
| `favorite` | 收藏数                       |
| `uid`      | 用户ID                       |
| `uname`    | 用户名                       |
| `tags`     | 标签                         |

```json
{
    "bid": "BV1P3411b7dY",
    "pic": "http://i2.hdslb.com/bfs/archive/9ac78e6bc9cdc4ca036104d964d4c3ab9e6c46d7.jpg",
    "title": "EDG-S11《ELOG》丨冠军背后",
    "pubdate": 1638057600000,
    "duration": 1603,
    "view": 1493857,
    "like": 77533,
    "coin": 57025,
    "share": 5777,
    "danmaku": 24004,
    "reply": 4206,
    "favorite": 21399,
    "uid": 31536760,
    "uname": "EDG电子竞技俱乐部",
    "tags": "LOL,英雄联盟,EDG,电子竞技,电竞,英雄联盟s11,EDG夺冠,为爱而聚，E起前进"
}
```



# up_info 需求分析
## 接口文档
###  1. 获取接口
### 接口文档

#### API: `/up`

**描述**: 查询 `up_info` 表并返回结果的 JSON 字符串。

**方法**: `GET`

```http
GET http://127.0.0.1:5000/up?name=新华社&fans=True
```

**参数**:

| 参数名称         | 参数类型    | 是否必填 | 参数描述                  |
|--------------|---------| --- |-----------------------|
| `name`       | string  | 否 | 使用全文搜索匹配 `name` 字段    |
| `profile`    | string  | 否 | 使用全文搜索匹配 `profile` 字段 |
| `fans_limit` | bigint  | 否 | 查询粉丝数量大于等于 `fans_limit` 的 UP 主 |                
| `likes`      | boolean | 否 | 如果为 `True`，按点赞数量降序排序  |
| `plays`      | boolean | 否 | 如果为 `True`，按播放数量降序排序  |
| `uid`        | string  | 否 | 精确匹配 `uid` 字段         |

**响应**:
**响应参数**:
**响应参数**:

返回的 JSON 数组包含以下字段：

| 字段名称      | 数据类型 | 描述         |
|-----------| --- |------------|
| `uid`     | string | UP主的唯一标识符  |
| `img_url` | text | UP主的头像 URL |
| `name`    | string | UP主的名称     |
| `profile` | string | UP主的简介     |
| `fans`    | integer | UP主的粉丝数量   |
| `likes`   | integer | UP主的点赞数量   |
| `plays`   | integer | UP主的播放数量   |
| `videos`  | integer | UP主的视频数量   |




每个对象表示一个符合查询条件的 UP 主的信息。示例响应中包含多个此类对象。


- `200 OK`: 返回查询结果的 JSON 字符串。
- `400 Bad Request`: 参数无效或请求错误。
- `500 Internal Server Error`: 服务器内部错误。

**示例请求**:

``` json
{"name":"新华社",
"img_url":"https://i1.hdslb.com/bfs/face/396b93a7f619882afa711879dbf2cb98a40e7367.jpg"
"profile":"我是稳中带皮皮中有稳稳得一皮的鲜花舍。本社专营各种新闻报道，欢迎各位选购。",
"fans":15941471,
"likes":198212715,
"plays":1923465765,
"uid":473837611}
```

# 弹幕获取

**API**：/danmaku

**描述：**
获取特定视频的所有弹幕

**方法**：`GET`
```http request
GET http://127.0.0.1:5000/danmu_wordcloud?bv=BV17b421e7Ei
```
**参数：**

| 参数名称 | 参数类型 | 是否必填 | 参数描述 |
|------|------|------|------|
|bv|string|是|需获得弹幕的视频的bv号|


**响应：**\
```json
{
    "image_url": "static/danmaku_wordcloud/BV1Uu4y1h7bd.png"
}
```


# 推荐视频


## 推荐视频 API

`GET /recommend_videos`

### 描述
此端点返回推荐视频列表。视频可以根据指定的分区进行过滤，或者显示所有分区的视频。

### 请求参数

| 参数        | 类型   | 是否必填 | 描述                                        |
|-------------|--------|------|-------------------------------------------|
| `partition` | String | 是    | 要过滤视频的分区名。可以是特定的分区名，或使用 "all" 来获取所有分区的视频。 |

### 示例请求

**GET 请求:**

```http
GET http://127.0.0.1:5000/recommend_videos?partition=all
```

#### 响应参数

| 参数名称  | 参数描述             |
|-------|------------------|
| `bid` | 视频ID             |
| `pic` | 封面图片URL          |
| `title` | 视频标题             |
| `pubdate` | 发布日期（Unix时间戳，毫秒） |
| `duration` | 视频时长（秒）          |
| `view` | 播放量              |
| `like` | 点赞数              |
| `coin` | 硬币数              |
| `share` | 分享数              |
| `danmaku` | 弹幕数              |
| `reply` | 评论数              |
| `favorite` | 收藏数              |
| `uid` | 用户ID             |
| `uname` | 用户名              |
| `tags` | 标签               |
 | `par` | 分区名              |
  | `rank` | 推荐视频的排名          |

```json
{"bid":"BV1Uu4y1h7bd",
 "pic":"http:\/\/i2.hdslb.com\/bfs\/archive\/610a8568f780aa0abc55cdddb1f1c09c8aa5a7f5.jpg",
 "title":"商标被抢注？影视飓风认识多少个UP主？700万粉丝Q&A！",
 "pubdate":1699045200000,
 "duration":786,
 "view":3524362,
 "like":293341,
 "coin":113086,
 "share":9366,
 "danmaku":21076,
 "reply":4388,
 "favorite":54510,
 "uid":946974,
 "uname":"影视飓风",
 "tags":"万物研究所,生活记录,4K,搞笑,UP主,吐槽,自媒体,干货,Q&A,健将,万物研究所·第11期",
 "par":"生活",
 "rank":6.8531941392
}
```



# 推荐UP主 API

### 端点
`GET /recommend_ups`

### 描述
此端点返回推荐的UP主列表。UP主可以根据指定的分区和排序方式进行过滤。

### 请求参数

| 参数        | 类型   | 是否必填 | 描述                                          |
|-------------|--------|------|---------------------------------------------|
| `partition` | String | 是    | 要过滤UP主的分区名。可以是特定的分区名，或使用 "all" 来获取所有分区的UP主。 |
| `order`     | String | 是    | 排序方式。可以是 `like` 根据点赞数排序，或 `inter` 根据互动数排序。  |

### 示例请求

**GET 请求:**

```http
GET http://127.0.0.1:5000/recommend_ups?partition=all&order=like
```
### 响应参数

| 字段名称      | 数据类型    | 描述         |
|-----------|---------|------------|
| `uid`     | string  | UP主的唯一标识符  |
| `img_url` | text    | UP主的头像 URL |
| `name`    | string  | UP主的名称     |
| `profile` | string  | UP主的简介     |
| `fans`    | integer | UP主的粉丝数量   |
| `likes`   | integer | UP主的点赞数量   |
| `plays`   | integer | UP主的播放数量   |
| `videos`  | integer | UP主的视频数量   |
| `par`     | string  | UP主的分区     |

```json
{"uid":151482404,
 "par":"知识",
 "name":"赛雷话车",
 "profile":"赛雷话车，爷爷看了都说懂",
 "fans":1849806,
 "likes":20902587,
 "plays":168116498,
 "videos":274,
 "img_url":"\/\/i2.hdslb.com\/bfs\/face\/a762bcb3b35ee903715102fae85a0cb9f0885d00.jpg@240w_240h_1c_1s_!web-avatar-space-header.avif"}
```


# 番剧查询接口文档

## 接口描述

该接口用于查询番剧信息，支持多种查询参数和排序方式。

## 请求URL

**GET**  `/bangumi`

## 请求参数

| 参数名       | 类型   | 是否必填 | 说明                                  |
|--------------|------|----------|-------------------------------------|
| name         | string | 否       | 番剧名称，模糊匹配                           |
| profile      | string | 否       | 番剧简介，模糊匹配                           |
| tags         | string | 否       | 标签，模糊匹配                             |
| fans_limit   | int  | 否       | 粉丝数下限                               |
| score_limit  | int  | 否       | 最低评分 (默认排序为score排序，score相同按照fans排序) |
| score_people | boolean | 否       | 按评分人数排序                             |
| danmaku      | boolean | 否       | 按弹幕数量排序                             |
| plays        | boolean | 否       | 按播放量排序                              |
| start_time   | string | 否       | 开始时间，格式为`YYYY-MM-DD HH:mm:ss`       |
| end_time     | string | 否       | 结束时间，格式为`YYYY-MM-DD HH:mm:ss`       |




## 请求示例

**GET** `/bangumi?name=JOJO&score_limit=8&start_time=2022-01-01 00:00:00&end_time=2022-12-31 23:59:59&plays=1`
## 响应参数

| 字段名          | 类型   | 说明   |
|--------------|--------|------|
| name         | string | 番剧名称 |
| profile      | string | 番剧简介 |
| tags         | string | 标签   |
| score        | float  | 评分   |
| score_people | int    | 评分人数 |
| start_time   | string | 开播时间 |
| danmaku      | int    | 弹幕数量 |
| fans         | int    | 追番人数 |
| plays        | int    | 播放量  |
| cover_url    | string | 封面图片 |

## 响应示例

```json
{"cover_url":"https:\/\/i0.hdslb.com\/bfs\/bangumi\/image\/14ccd8457a9b7351e7be1d87db2719791108ddc0.png@338w_450h.webp",
 "name":"JOJO的奇妙冒险石之海",
 "tags":"漫画改,热血,战斗,奇幻",
 "plays":310000000,
 "fans":31000,
 "danmaku":1617000,
 "score":9.8,
 "score_people":101326,
 "start_time":1669852800000,
 "profile":"简介：西历2011年，美国·佛罗里达州。在与恋人兜风途中遇到了交通事故的空条徐伦，因被陷害而获刑15年。收容设施是州立绿海豚街重警备监狱——别名「水族馆」。深陷绝望之中的徐伦，在手握父亲所托的吊坠时，她觉醒了不可思议的力量。“这个世界上存在着比死还恐怖的事情，而这一切都将在这所监狱中发生”徐伦面前出现的神秘少年所传达的信息，不断发生的不可思议的事件，前来探视的父亲·空条承太郎所说的令人恐惧的现实，以及名为DIO之人……空条徐伦究竟能否从这所「石之海」一般的监狱中重获自由？给持续百年之久的乔斯达一族与DIO之间的宿命画上..."
}
```