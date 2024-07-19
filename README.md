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
GET http://127.0.0.1:5000/danmu_wordcloud?bv=BV17b421e7Ei&date=2024-7-16
```
**参数：**

| 参数名称 | 参数类型 | 是否必填 | 参数描述 |
|------|------|------|------|
|bv|string|是|需获得弹幕的视频的bv号|
|date|string|是|YYYY-MM-DD格式的当前日期|

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


