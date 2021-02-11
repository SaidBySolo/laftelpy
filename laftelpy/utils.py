from inspect import getfullargspec
from laftelpy.typing import CompareList, SearchParameters
from typing import Any, Callable, Optional, get_args


def convert_params(param_value: Optional[bool]) -> Optional[str]:
    if param_value is None:
        return None
    else:
        return str(param_value).lower()


def compare(arg: CompareList, exclude_arg: CompareList):
    if arg_list := list(set(arg) & set(exclude_arg)):
        raise ValueError(
            f"Items to be excluded and items to be included cannot come together: {arg_list}"
        )


def join_params(params: SearchParameters):
    for key, value in params.items():
        if isinstance(value, list):
            if 1 < len(value):
                params[key] = ",".join(value)
            else:
                params[key] = "".join(value)

    return params


def check_arg(
    func: Callable[[Any], Any],
    local_args: SearchParameters,
):
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
