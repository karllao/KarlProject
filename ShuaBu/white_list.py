# 白名单配置 - 用于shuabu.py调用

# 用户白名单
USER_WHITELIST = [
    '16611118888',
    '18811112222',
    '7777777@qq.com']

def is_user_allowed(user: str) -> bool:
    """检查用户是否在白名单中"""
    return user in USER_WHITELIST