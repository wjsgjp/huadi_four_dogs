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




 # user_analys  需求分析
## 接口文档


