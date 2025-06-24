import asyncio
from dataclasses import dataclass
from datetime import datetime
import random

from linq.linq import linq


@dataclass
class Test:
    i: int
    s: str


async def main() -> None:
    src: list[Test] = []
    for i in range(12):
        src.append(Test(i, (2**i).__str__()))
        random.seed(datetime.now().microsecond)
        await asyncio.sleep(0.01)

    src2 = linq[Test](src)
    print("src:", src2.to_list())
    print("count:", src2.count(lambda e: e.i % 2 == 0))
    print("any:", src2.any(lambda e: e.s == (2**7).__str__()))
    print("where:", src2.where(lambda e: e.i % 2 == 0).to_list())
    print("select:", src2.select(lambda e: e.s).to_list())
    print("first:", src2.first())
    print("firstdef:", src2.first_or_default(v=Test(0, "first_def")))
    print("last:", src2.last())
    print("lastdef:", src2.last_or_default(v=Test(0, "last_def")))
    print("list:", list(src2))


if __name__ == "__main__":
    asyncio.run(main())
