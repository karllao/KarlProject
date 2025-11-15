#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
示例脚本：展示如何在 Python 代码中调用主函数
"""

from main import main

def example1_basic():
    """示例1：基础用法 - 单账号"""
    print("=" * 60)
    print("示例1：基础用法 - 单账号")
    print("=" * 60)
    
    config = {
        "USER": "user@example.com",
        "PWD": "your_password",
        "MIN_STEP": "18000",
        "MAX_STEP": "25000"
    }
    
    main(config_data=config)


def example2_with_aes_key():
    """示例2：使用 AES 密钥加密保存令牌"""
    print("=" * 60)
    print("示例2：使用 AES 密钥加密保存令牌")
    print("=" * 60)
    
    config = {
        "USER": "user@example.com",
        "PWD": "your_password",
        "MIN_STEP": "18000",
        "MAX_STEP": "25000"
    }
    
    # AES 密钥必须是16个字符
    aes_key = "1234567890123456"
    
    main(config_data=config, aes_key_str=aes_key)


def example3_multiple_accounts():
    """示例3：多账号运行"""
    print("=" * 60)
    print("示例3：多账号运行（用#分隔）")
    print("=" * 60)
    
    config = {
        "USER": "user1@example.com#user2@example.com#13800138000",
        "PWD": "password1#password2#password3",
        "MIN_STEP": "18000",
        "MAX_STEP": "25000",
        "SLEEP_GAP": "5",  # 账号之间间隔5秒
        "USE_CONCURRENT": "False"  # 不使用并发
    }
    
    main(config_data=config)


def example4_with_pushplus():
    """示例4：启用 PushPlus 推送"""
    print("=" * 60)
    print("示例4：启用 PushPlus 推送")
    print("=" * 60)
    
    config = {
        "USER": "user@example.com",
        "PWD": "your_password",
        "MIN_STEP": "18000",
        "MAX_STEP": "25000",
        "PUSH_PLUS_TOKEN": "your_pushplus_token",  # 从 https://www.pushplus.plus/ 获取
        "PUSH_PLUS_HOUR": "22",  # 仅在北京时间22点推送
        "PUSH_PLUS_MAX": "30"
    }
    
    main(config_data=config)


def example5_with_concurrent():
    """示例5：多账号并发运行"""
    print("=" * 60)
    print("示例5：多账号并发运行（加速执行）")
    print("=" * 60)
    
    config = {
        "USER": "user1@example.com#user2@example.com#user3@example.com",
        "PWD": "password1#password2#password3",
        "MIN_STEP": "18000",
        "MAX_STEP": "25000",
        "USE_CONCURRENT": "True"  # 启用多线程
    }
    
    main(config_data=config)


def example6_from_json_string():
    """示例6：从 JSON 字符串配置"""
    print("=" * 60)
    print("示例6：从 JSON 字符串配置")
    print("=" * 60)
    
    config_json = '{"USER":"user@example.com","PWD":"password","MIN_STEP":"18000","MAX_STEP":"25000"}'
    
    main(config_data=config_json)


def example7_complete_config():
    """示例7：完整配置 - 所有选项"""
    print("=" * 60)
    print("示例7：完整配置 - 包含所有可选项")
    print("=" * 60)
    
    config = {
        "USER": "user1@example.com#user2@example.com",
        "PWD": "password1#password2",
        "MIN_STEP": "18000",
        "MAX_STEP": "25000",
        "PUSH_PLUS_TOKEN": "your_token",
        "PUSH_PLUS_HOUR": "22",
        "PUSH_PLUS_MAX": "30",
        "SLEEP_GAP": "5",
        "USE_CONCURRENT": "False"
    }
    
    aes_key = "1234567890123456"
    
    main(config_data=config, aes_key_str=aes_key)


if __name__ == "__main__":
    import sys
    
    print("\n" + "=" * 60)
    print("小米运动自动刷步数 - Python 调用示例")
    print("=" * 60 + "\n")
    
    print("可用的示例函数：")
    print("  1. example1_basic() - 基础用法")
    print("  2. example2_with_aes_key() - 使用AES密钥")
    print("  3. example3_multiple_accounts() - 多账号")
    print("  4. example4_with_pushplus() - PushPlus推送")
    print("  5. example5_with_concurrent() - 并发运行")
    print("  6. example6_from_json_string() - JSON字符串配置")
    print("  7. example7_complete_config() - 完整配置")
    print("\n请修改配置后选择运行相应的函数。\n")
    
    # 这里可以手动调用任何示例函数
    # 例如：example1_basic()
    
    print("提示：在实际使用时，请修改相应配置并调用对应的函数。")
    print("      或者使用命令行：python main.py --help 查看详细说明。\n")
