# 一、环境配置

### 先安装uv
macos
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

windows
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 白名单配置
> /ShuaBu/white_list.py - USER_WHITELIST

### 初次运行虚拟环境配置
```
uv venv

linux/macos: source .venv/bin/activate
windows: .\.venv\Scripts\activate

uv pip install -e .
```

# 二、数据库配置

> /KarlProject/setting.py - DATABASES

# 三、数据库初始化

### 创建基础表结构

```
python3 manage.py migrate
```

### 让 Django 知道我们在我们的模型有一些变更

```
python3 manage.py makemigrations ShuaBu
```

### 创建表结构

```
python3 manage.py migrate ShuaBu
```



# 运行
```
uv run manage.py runserver 0.0.0.0:8000
```

### 配置域名
无域名可忽略
> /KarlProject/setting.py - CSRF_TRUSTED_ORIGINS