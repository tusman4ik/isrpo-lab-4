# Описание решение
Библиотека включает в себя модули для вычисления площадей и периметров геометрических 
фигур: квадрата и круга

# Функции
## circle.py
- `area(r: (float|int))->(float|int)` - Функция принимает на вход радиус круга и возвращает его площадь.
    ```python
    from circle import area
    area(5) #return: 49.298
    ```
- `perimeter(r: (float|int))->(float|int)` - Функция принимает на вход радиус круга и возвращает его периметр. Пример: `perimeter() #`
    ```python
    from circle import area
    area(5) #return: 31.4
    ```
## square.py
- `area(r: (float|int))->(float|int)` - Функция принимает на вход сторону квадрата и возвращает его площадь. 
    ```python
    from square import area
    area(5) #return: 25
    ```
- `perimeter(r: (float|int))->(float|int)` - Функция принимает на вход сторону квадрата и возвращает его периметр. 
    ```python
    from square import area
    area(5) #return: 20
    ```
# История изменений
```
* commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (HEAD -> main, origin/main, origin/HEAD)
| Author: smartiqa <info@smartiqa.ru>
| Date:   Thu Mar 4 14:55:29 2021 +0300
| 
|     L-03: Docs added
| 
* commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
  Author: smartiqa <info@smartiqa.ru>
  Date:   Thu Mar 4 14:54:08 2021 +0300
  
      L-03: Circle and square added
```

