"""
ombie 骰子模拟器
骰子游戏 Zombie Dice 的模拟器，可以运行机器人 AI 玩家。

Zombie Dice 是 Steve Jackson Games 推出的一款快速、有趣的骰子游戏。 玩家扮演僵尸，试图吃掉尽可能多的人类大脑而不被人类“猎枪射击”。 轮到玩家时，玩家将从十三个骰子中随机选择三个骰子并掷骰子。 骰子的面孔是大脑、脚步声和霰弹枪。 每个大脑你得一分，但如果你累计掷出三把霰弹枪，你就会被霰弹枪击中，并在你的回合中获得零分。 然后，您可以决定重新滚动或将轮到下一位玩家。 如果骰子作为“脚步声”出现，如果玩家决定重新掷骰子，则会再次使用它。 （玩家每次掷骰子总是使用三个骰子。）僵尸骰子有一个“推你的运气”游戏机制：你选择重新掷骰子的次数越多，你可以获得的大脑就越多，但你收集的可能性就越大 三把霰弹枪。 游戏持续进行，直到一名玩家达到 13 个大脑，然后其余玩家再进行一轮。 骰子颜色为绿色（大脑的可能性更大）、红色（霰弹枪的可能性更大）和黄色（大脑和霰弹枪的可能性相等）。

更完整的僵尸骰子规则可以在这里找到：

英文版规则 PDF
Flash 动画演示如何玩
带有规则的指导性文章
有人解释规则的 YouTube 视频
该模拟器对于初级/中级编程课程或竞赛很有用。 用于制作机器人的 API 很简单，并且它具有一个 Web UI，用于在锦标赛运行时投射漂亮的显示。

"""