'''
Датасет тут: 
https://github.com/ivan001422/AI-learning/blob/main/Datasets/Iris
'''

class Sample:
    def __init__(
            self,
            sepal_length: float,
            sepal_width: float,
            petal_length: float,
            petal_width: float,
            species=None
    ) -> None:
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species
        self.classification = None

    def classify(self, label: str) -> None:
        self.classification = label

    def matches(self) -> bool:   
        return self.classification == self.species

    def __repr__(self) -> str:
        # Возвращаем строку, похожую на конструктор, чтобы было ясно, что за объект
        return (
            f"Sample(sepal_length={self.sepal_length}, "
            f"sepal_width={self.sepal_width}, "
            f"petal_length={self.petal_length}, "
            f"petal_width={self.petal_width}, "
            f"species={self.species!r}, "
            f"classification={self.classification!r})"
        )

class Hyperparameter:
    def __init__(self, k: int, test_samples: list) -> None:
        self.k = k
        self.test_samples = test_samples
        self.quality = 0

    def test(self) -> None:
        correct = 0
        for sample in self.test_samples:
            guess = self.classify(sample)
            sample.classify(guess)
            correct += sample.matches()
        self.quality = correct / len(self.test_samples)

    def classify(self, sample: Sample) -> str:
        # Заглушка
        return 'virginica'


class Training_Data:
    def __init__(self, name: str) -> None:
        self.name = name
        self.training = []
        self.test = []
        self.tuning = []

    def load(self, path: str) -> None:
        file = open(path)
        file.readline()
        cnt = 0
        for line in file:
            cnt += 1
            parts = line.split(',')
            sepal_length = float(parts[0])
            sepal_width = float(parts[1])
            petal_length = float(parts[2])
            petal_width = float(parts[3])
            species = parts[4].strip()   # очистка от пробелов и \n
            sample = Sample(sepal_length, sepal_width, petal_length, petal_width, species)
            if cnt % 4 == 0:
                self.test.append(sample)
            else:
                self.training.append(sample)

    def testing(self, hyperparameter: Hyperparameter) -> None:
        hyperparameter.test()
        self.tuning.append(hyperparameter)


# ---------- Использование ----------
data = Training_Data('Data')
data.load('.venv/Data')

print(f"Обучающих: {len(data.training)}")
for i in data.training[:3]:
    print(i)
print(f"\nТестовых: {len(data.test)}")
for i in data.test[:3]:
    print(i)
# Посмотрим, какие виды есть в тесте
print("\nВиды в тесте:", set(s.species for s in data.test))

hp1 = Hyperparameter(k=3, test_samples=data.test)
data.testing(hp1)

print(f"k={data.tuning[0].k}, quality={data.tuning[0].quality:.2%}")
