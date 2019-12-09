# pytest-crontab

Pytest注册crontab 任务

---

### 如何使用

1. 安装 `pytest-crontab`

```
pip install pytest-crontab
```

2. 使用方法

或命令行传入
```
$ pytest --crontab='*/1 * * * *'
```
> 注册在crontab中的任务默认使用pytest .运行所有

crontab -l 查看任务
```
*/1 * * * * cd /root; pytest . >>pytest.log
```

> 目前仅支持CentOS
---

- Email: <a href="mailto:superhin@126.com?Subject=Pytest%20Email" target="_blank">`superhin@126.com`</a> 
- Blog: <a href="https://www.cnblogs.com/superhin/" target="_blank">`博客园 韩志超`</a>
- 简书: <a href="https://www.jianshu.com/u/0115903ded22" target="_blank">`简书 韩志超`</a>

