class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""
    M_IN_KM: int = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 LEN_STEP: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.LEN_STEP = LEN_STEP
        pass

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return ((self.action*self.LEN_STEP / M_IN_KM)) 
        pass

    def get_mean_speed(self) -> float:
        return self.get_distance() / self.duration
        """Получить среднюю скорость движения."""
        pass

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""
    def get_spent_calories(self) -> float:
        run_cal_1: int = 18
        run_cal_2: int = 20
        (run_cal_1 * self.get_mean_speed() - run_cal_2) * self.weight / M_IN_KM * self.duration 
    pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    super().__init__(Training, height: float)
    self.height = height
    def get_spent_calories(self) -> float:
        walc_cal_1: float = 0.035
        walc_cal_2: float = 0.029
        walc_cal_1

    pass


class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

