# up video 需求分析

## 接口文档

### 1. 获取接口
**接口名称**：获取筛选视频信息  
**接口地址**：`/up/videos`  
**请求方式**：GET  

#### 请求参数

| 参数名称          | 参数类型 | 是否必填 | 参数描述                   |
|-------------------|----------|----------|----------------------------|
| `bid`             | string   | 否       | 视频ID                     |
| `title`           | string   | 否       | 视频标题                   |
| `pubdate_start`   | string   | 否       | 开始发布日期，格式为YYYY-MM-DD HH:MM:SS |
| `pubdate_end`     | string   | 否       | 结束发布日期，格式为YYYY-MM-DD HH:MM:SS |
| `duration_min`    | int      | 否       | 最小时长                   |
| `duration_max`    | int      | 否       | 最长时长                   |
| `view`            | boolean  | 否       | 是否按播放量排序           |
| `like`            | boolean  | 否       | 是否按点赞量排序           |
| `coin`            | boolean  | 否       | 是否按投币量排序           |
| `share`           | boolean  | 否       | 是否按分享量排序           |
| `danmaku`         | boolean  | 否       | 是否按弹幕量排序           |
| `reply`           | boolean  | 否       | 是否按评论量排序           |
| `favorite`        | boolean  | 否       | 是否按收藏量排序           |
| `uname`           | string   | 否       | UP主名称                   |
| `tags`            | string   | 否       | 视频标签                   |
| `date_order_desc` | boolean  | 否       | 是否按发布日期降序排序     |
| `date_order_asc`  | boolean  | 否       | 是否按发布日期升序排序     |

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