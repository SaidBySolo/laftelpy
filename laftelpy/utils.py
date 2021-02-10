from typing import Any, Callable, Optional, get_args
from inspect import getfullargspec


def convert_params(param_value: Optional[bool]) -> Optional[str]:
    if param_value is None:
        return
    else:
        return str(param_value).lower()


def compare(arg: list[str], exclude_arg: list[str]):
    if arg_list := list(set(arg) & set(exclude_arg)):
        raise ValueError(
            f"Items to be excluded and items to be included cannot come together: {arg_list}"
        )


def join_params(params: dict[str, Any]):
    for k, v in params.items():
        if isinstance(v, list):
            if 1 < len(v):
                params[k] = ",".join(v)
            else:
                params[k] = "".join(v)

    return params


def check_arg(func: Callable[[Any], Any], local_args: dict[str, Any]):
    fullarg = getfullargspec(func)
    del local_args["self"]
    annotations = fullarg.annotations

    for l, a in zip(local_args.values(), annotations.values()):
        a = get_args(a)
        if isinstance(l, str):
            if l not in a:
                raise ValueError(
                    f"The arguments do not match. Expected argument: {a} Arguments received: '{l}'"
                )

        if isinstance(l, list):
            a = get_args(a[0])
            if between := tuple((set(l) - set(a))):
                raise ValueError(
                    f"The arguments do not match. Expected argument: {a} Arguments received: {between}"
                )
