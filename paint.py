from point import Point
from rect import Rect


def test_bound_instance_method():
    p = Point()
    p.set_x(10)
    p.set_y(20)
    # print(p.get_x(), p.get_y())
    p.show()
    print(p.count_of_instance)


def test_unbound_class_method():
    p = Point()
    Point.set_x(p, 10)
    Point.set_y(p, 20)
    print(Point.get_x(p), Point.get_y(p))


def test_othermethod():
    Point.class_method()
    Point.static_method()


def test_constructor():
    p1 = Point()
    Point.class_method()

    p2 = Point(10, 20)
    Point.class_method()

    p1.show()

    # p1 객체 삭제
    del p1
    Point.class_method()

    p2.show()


def test_to_string():
    p = Point(10, 20)
    print(p)
    print(repr(p))

    p2 = eval(repr(p))
    print(p2)


def test_class_rect():
    r1 = Rect(10, 10, 50, 50)
    r2 = eval(repr(r1))

    print(r1, r1.area(), sep=':')
    print(r2, r2.area(), sep=':')

    r1.draw()
    r2.draw()


def main():
    # test_othermethod()
    # test_unbound_class_method()
    # test_bound_instance_method()
    # test_constructor()
    # test_to_string()
    test_class_rect()


if __name__ == '__main__':
    main()




