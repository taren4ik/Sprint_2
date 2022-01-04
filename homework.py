class InfoMessage:
    """Информационное сообщение о тренировке."""
    def _init__(self,
                training_type: str,
                duration: float,
                distance: float,
                speed: float,
                calories: float
                ) -> None:
        self.training_type = training_type
        self.duration: float = duration
        self.distance: float = distance
        self.speed: float = speed
        self.calories: float = calories

    def get_message(self) -> str:
        training_type = self.training_type
        duration = round(self.duration, 3)
        distance = round(self.distance, 3) 
        speed = round(self.speed, 3)
        calories = round(self.calories, 3)

        msg: str = (f'Тип тренировки: {training_type};'
        f'Длительность: {duration} ч.; Дистанция: {distance} км;' 
        f'Ср. скорость: {speed} км/ч; Потрачено ккал: {calories}.')
        return msg


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    M_IN_KM: int = 1000
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight


    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        dist: float = self.action * self.LEN_STEP / self.M_IN_KM
        return dist

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return  self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        obj = InfoMessage()
        return obj.get_message()


class Running(Training):
    """Тренировка: бег."""  
    def get_spent_calories(self) -> float:
        run_cal_1: int = 18
        run_cal_2: int = 20
        return ((run_cal_1 * super().get_mean_speed() - run_cal_2) *
        self.weight / Training.M_IN_KM * (self.duration * 60))
 
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action,
                 duration,
                 weight
                 )
        self.height = height
       
    
    def get_spent_calories(self) -> float:
        walc_cal_1: float = 0.035
        walc_cal_2: float = 0.029
        walc_cal_3: int = 2
        return ((walc_cal_1 * self.weight + 
        (super().get_mean_speed()**walc_cal_3 // self.height)
        * walc_cal_2 * self.weight) * self.duration * 60)


class Swimming(Training):
    """Тренировка: плавание."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float) -> None:

        super().__init__(action,
                 duration,
                 weight
                 )
        self.length_pool = length_pool
        self.count_pool = count_pool
        self.LEN_STEP = 1.38


    def get_mean_speed(self) -> float:
        return (self.length_pool * self.count_pool / Training.M_IN_KM /
        self.duration)
 
    def get_spent_calories(self) -> float:
        swim_cal_1: float = 1.1
        swim_cal_2: float = 2
        return (self.get_mean_speed() + swim_cal_1) * swim_cal_2 * self.weight


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    dic_wtype: dict= {
    'SWM': 'Swimming',
    'RUN': 'Running',
    'WLK': 'SportsWalking'
    } 
    return dic_wtype[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    return print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

