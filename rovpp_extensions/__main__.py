import time

from .sims import (
    run_fig678,
    run_fig9,
    run_fig10,
)

def main():
    sim_funcs = (
        run_fig678,
        run_fig9,
        run_fig10,
    )

    for sim_func in sim_funcs:
        start = time.perf_counter()
        sim_func()  # type: ignore
        print(f"{time.perf_counter() - start}s for {getattr(sim_func, '__name__', '')}")


if __name__ == "__main__":
    main()
