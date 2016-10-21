#include <cmath>

template<typename T>
class Vector
{
 public:
    T x, y;

    Vector(T x, T y)
    {
        this->x = x;
        this->y = y;
    }

    Vector(Vector<T> a, Vector<T> b)
    {
        this->x = b.x - a.x;
        this->y = b.y - a.y;
    }
    
    Vector() {}

    double len()
    {
        return sqrt(sqr(x) + sqr(y));
    }

    Vector<double> just_direction()
    {
        return Vector<double>(x / len(), y / len());
    }

    Vector<T> normal()
    {
        return Vector<T>(-y, x);
    }

    T dot_product(Vector<T> sec)  // скалярное
    {
        return x * sec.x + y * sec.y;  // Если угол тупой/прямой/острый, то произведение меньше/равно/больше нуля.
    }

    T cross_product(Vector<T> sec)  // векторное
    {
        return x * sec.y - sec.x * y;  // Ориентированная площадь параллелограмма.
        // Положительна = второй вектор направлен левее первого.
        // Равна нулю = второй вектор направлен так же / противоположно первому.
        // Отрицательна = второй вектор направлен правее первого.
    }

    //TODO: наклон вектора на произвольный угол
    // x = x * cos(alpha) + y * sin(alpha)
    // y = -x * sin(alpha) + y * cos(alpha)

    //TODO: биссектриса: полусумма нормированных векторов.
};

typedef Vector Point;

class Line
{
 public:

    double a, b, c;  // ax + by + c = 0

    Line(double a, double b, double c)
    {
        this->a = a;
        this->b = b;
        this->c = c;
    }

    Line(Point fir, Point sec)
    {
        this->a = fir.y - sec.y;
        this->b = sec.x - fir.x;
        this->c = sec.y * x - sec.x * y;
    }

    Line() {}

    double distance(Point p)
    {
        return (a * p.x + b * p.y + c) / sqrt(sqr(a) + sqr(b));
    }

    //TODO: Параллельное смещение прямой
};

class Circle
{
 public:
    Circle() {}
};

// class Polygon
