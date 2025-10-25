## Hot Trends Analysis Resolve

> [!CAUTION]
> 本项目单纯包装了一下脚本，通过网页方便调用和查看。**安全意识个个皆无，开发规范项项违反**，是典型的安全灾难级项目，因此严禁将此项目直接部署到公网。**若有必要，请务必设置附加认证**。

使用本地部署的 [DailyHotApi](https://github.com/imsyy/DailyHotApi) 与 [Ollama](https://ollama.com/) 实现用 AI 分析当下热点。

该仓库为项目前端，后端参见[后端仓库](https://github.com/sixiaolong1117/hot-trends-analysis-backend)。

### 使用方法

使用 Docker Compose 部署：

```yml
services:
  dailyhotapi:
    image: imsyy/dailyhot-api:latest
    container_name: dailyhot-api
    restart: always
    ports:
      - "6688:6688"
    environment:
      - DNS=223.5.5.5,8.8.8.8
      - TZ=Asia/Shanghai
  hot-trends-analysis-resolve:
    image: ghcr.io/sixiaolong1117/hot-trends-analysis-resolve:latest
    container_name: hot-trends-analysis-resolve
    restart: always
    ports:
      - "8080:8080"
    volumes:
      - ./outputs:/data:ro
    environment:
      - TZ=Asia/Shanghai
      - PORT=8080
      - DATA_DIR=/data
    healthcheck:
      test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')"]
      interval: 30s
      timeout: 3s
      retries: 3
  hot-trends-analysis-backend:
    image: ghcr.io/sixiaolong1117/hot-trends-analysis-backend:latest
    container_name: hot-trends-analysis-backend
    restart: always
    ports:
      - "8000:8000"    
    volumes:
      - ./outputs:/app/outputs           
    environment:
      - TZ=Asia/Shanghai      
      - OLLAMA_API=http://192.168.0.2:11434     
      - HOT_SEARCH_API=http://dailyhotapi:6688
      - TOPICS_PER_PLATFORM=10
      - DEFAULT_PLATFORMS=36kr,51cto,52pojie,acfun,baidu,bilibili,coolapk,csdn,dgtle,douban-group,douban-movie,douyin,earthquake,gameres,geekpark,genshin,github,guokr,hackernews,hellogithub,history,honkai,hostloc,hupu,huxiu,ifanr,ithome-xijiayi,ithome,jianshu,juejin,kuaishou,linuxdo,lol,miyoushe,netease-news,newsmth,ngabbs,nodeseek,nytimes,producthunt,qq-news,sina-news,sina,smzdm,sspai,starrail,thepaper,tieba,toutiao,v2ex,weatheralarm,weibo,weread,yystv,zhihu-daily,zhihu
      # DEFAULT_PLATFORMS 保留你需要的，不建议太多，输入热搜条目太多太杂容易让 LLM 产生更严重的幻觉。
      # 有关所有接口名对应的网站，见：https://github.com/imsyy/DailyHotApi?tab=readme-ov-file#-%E6%8E%A5%E5%8F%A3%E6%80%BB%E8%A7%88
```

使用 `http://<IP>:8000` 访问后端界面，调整需要的平台、模型等参数，点击“开始分析”，即可自动拉取热搜内容并通过 AI 分析当下热点。

使用 `http://<IP>:8080` 访问前端界面，即可以图形化格式查看分析结果。

### 进阶使用

本项的核心实际上是[后端分析脚本](https://github.com/sixiaolong1117/hot-trends-analysis-backend/blob/master/app/analyzer.py)，该脚本完全可以直接单独使用，通过计划任务等方式调用。