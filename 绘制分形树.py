"""
    功能：绘制分形树
    环境：python3.7
    日期：2019/1/14 20:13
    作者：指尖魔法师
    版本：1.0
"""
import turtle as t


def draw_tree(size):
    """
    分形树的绘制函数
    """
    if size < 20:
        t.pencolor("green")
    else:
        t.pencolor("brown")

    if size > 5:
        # 绘制右边分支

        t.forward(size)
        t.right(20)
        draw_tree(size-5)

        # 绘制左边分支
        t.left(40)
        draw_tree(size-5)

        # 返回原点
        t.right(20)
        t.penup()
        t.backward(size)
        t.pendown()


def main():
    """
    主函数
    """
    t.left(90)
    t.penup()
    t.backward(100)
    t.pendown()
    length = 50
    t.pensize(2)
    t.pencolor("brown")
    t.speed(5)

    # 调用分形树函数
    draw_tree(length)

    t.exitonclick()


if __name__ == '__main__':
    main()

