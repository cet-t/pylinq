from typing import Callable, Generic, Iterator, TypeVar

T_SRC = TypeVar("T_SRC")
T_RLT = TypeVar("T_RLT")

PRED = Callable  # Func


class linq(Generic[T_SRC]):
    def __init__(self, src: list[T_SRC] | Iterator[T_SRC]) -> None:
        self.__src = list(src)

    def __iter__(self) -> Iterator[T_SRC]:
        for e in self.__src:
            yield e

    def any(self, pred: PRED[[T_SRC], bool] | None = None) -> bool:
        if pred is None:
            return bool(self.__src)

        for e in self.__src:
            if pred(e):
                return True
        return False

    def count(self, pred: PRED[[T_SRC], bool] | None = None) -> int:
        if pred is None:
            return self.__src.__len__()
        return [None for e in self.__src if pred(e)].__len__()

    def where(self, pred: PRED[[T_SRC], bool]) -> "linq[T_SRC]":
        return linq([e for e in self.__src if pred(e)])

    def select(self, pred: PRED[[T_SRC], T_RLT]) -> "linq[T_RLT]":
        return linq([pred(e) for e in self.__src])

    def find_index(self, pred: PRED[[T_SRC], bool]) -> int:
        for i, e in enumerate(self.__src):
            if pred(e):
                return i
        return -1

    def find(self, pred: PRED[[T_SRC], bool]) -> T_SRC | None:
        return self.__src[i] if (i := self.find_index(pred)) != -1 else None

    def first_or_default(
        self,
        pred: PRED[[T_SRC], bool] | None = None,
        v: T_SRC | None = None,
    ) -> T_SRC | None:
        if pred is None:
            return self.__src[0]
        for e in self.__src:
            if pred(e):
                return e
        return v

    def first(
        self,
        pred: PRED[[T_SRC], bool] | None = None,
    ) -> T_SRC | None:
        return self.first_or_default(pred, None)

    def last_or_default(
        self,
        pred: PRED[[T_SRC], bool] | None = None,
        v: T_SRC | None = None,
    ) -> T_SRC | None:
        return linq(self.__src.__reversed__()).first_or_default(pred, v)

    def last(
        self,
        pred: PRED[[T_SRC], bool] | None = None,
    ) -> T_SRC | None:
        return self.last_or_default(pred, None)

    def to_list(self) -> list[T_SRC]:
        return self.__src

    @staticmethod
    def repeat(e: T_SRC, c: int) -> list[T_SRC]:
        return [e for _ in range(c)]

    @staticmethod
    def range(c: int) -> list[int]:
        return [i for i in range(c)]
