# def safe_division_b(number,divisor,ignore_overflow=False,ignore_zero_divison=False):
#     try:
#         return number/divisor
#     except OverflowError:
#         if ignore_overflow:
#             return 0
#         else:
#             raise
#     except ZeroDivisionError:
#         if ignore_zero_divison:
#             return float('inf')
#         else:
#             raise


def safe_division_b(number,divisor,*,ignore_overflow=False,ignore_zero_divison=False):
    try:
        return number/divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_divison:
            return float('inf')
        else:
            raise
ans=safe_division_b(1,10**500,ignore_overflow=True)
ans2=safe_division_b(1,0,ignore_zero_divison=True)
ans3=safe_division_b(1,0,True,True)
print(ans,ans2,ans3)


