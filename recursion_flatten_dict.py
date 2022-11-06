# def flatten_dict(dd, separator='_', prefix=''):
#     return {prefix + separator + k if prefix else k: v
#             for kk, vv in dd.items()
#             for k, v in flatten_dict(vv, separator, kk).items()
#             } if isinstance(dd, dict) else {prefix: dd}


def flatten_dict(d: dict, prefix: str = '') -> dict:
    result = {}
    separator = '_'
    if isinstance(d, dict):
        for k, v in d.items():
            for kk, vv in flatten_dict(d[k], k).items():
                if prefix:
                    result[prefix + separator + kk] = vv
                else:
                    result[kk] = vv
        return result
    else:
        return {prefix: d}


nested = {'Germany': {'berlin': 7}, 'Europe': {'italy': {'Rome': 3}}, 'USA': {'washington': 1, 'New York': 4}}

print(flatten_dict(nested))

for i in nested.items():
    print(i)
