
#include <iostream>
#include <string>
using namespace std;

/*
    интерфейсы
*/

class IBicycle { 

public:
    void virtual TwistTHeWheel() = 0;
    void virtual Ride() = 0;

};


class SimpleBicycle : public IBicycle {
public:
    void TwistTHeWheel() override {

        cout << "метод TwistTHeWheel() SimpleBicycle" << endl;

    }
    void Ride() override {

        cout << "метод Ride() SimpleBicycle" << endl;

    }
};


class SportBicycle : public IBicycle {
    void TwistTHeWheel() override {

        cout << "метод TwistTHeWheel() SimpleBicycle" << endl;

    }
    void Ride() override {

        cout << "метод Ride() SimpleBicycle" << endl;

    }
};


class Human {
public:
    void RideOn(IBicycle & bicycle) {
        cout << "Крути руль" << endl;
        bicycle.TwistTHeWheel();
        cout << endl << "Поехали" << endl;
        bicycle.Ride();
    }

};

int main()
{
    setlocale(LC_ALL, "ru");
    SimpleBicycle sb;
    SportBicycle sportB;

    Human h;
    h.RideOn(sportB);

    return 0;
}

