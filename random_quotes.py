import random
import time
from datetime import datetime

def generate_lucky_number():
    """生成今日幸运数字"""
    return random.randint(1, 99)

def get_random_color():
    """返回一个随机颜色"""
    colors = [
        '🔴 红色', '🟣 紫色', '🟡 黄色',
        '🟢 绿色', '🔵 蓝色', '⚪ 白色'
    ]
    return random.choice(colors)

def get_random_quote():
    """返回一句随机名言"""
    quotes = [
        '世上无难事，只要肯登攀。',
        '千里之行，始于足下。',
        '学而不思则罔，思而不学则殆。',
        '不积跬步，无以至千里。',
        '工欲善其事，必先利其器。',
        '失败是成功之母。',
        '天道酬勤。',
        '有志者事竟成。'
    ]
    return random.choice(quotes)

def get_random_activity():
    """推荐一个随机活动"""
    activities = [
        '☕ 和朋友喝咖啡',
        '📚 读一本好书',
        '🎮 玩一个小游戏',
        '🏃 出去散步',
        '🎵 听一首喜欢的歌',
        '✍️ 写一篇日记',
        '🧘 冥想放松一下',
        '📱 给老朋友打个电话'
    ]
    return random.choice(activities)

def generate_daily_fortune():
    """生成今日运势"""
    now = datetime.now()
    print(f"\n=== 🌟 {now.strftime('%Y年%m月%d日')} 今日运势 🌟 ===\n")
    print(f"🔮 幸运数字：{generate_lucky_number()}")
    print(f"🎨 幸运颜色：{get_random_color()}")
    print(f"💭 今日格言：{get_random_quote()}")
    print(f"📅 推荐活动：{get_random_activity()}")
    print("\n祝您度过愉快的一天！✨\n")

def main():
    """主函数"""
    print("欢迎使用每日运势生成器！")
    print("正在召唤神龙... 🐉")
    
    # 添加一个简单的加载动画
    for _ in range(3):
        print(".", end='')
        time.sleep(0.5)
    print("\n")
    
    generate_daily_fortune()

if __name__ == "__main__":
    main()
