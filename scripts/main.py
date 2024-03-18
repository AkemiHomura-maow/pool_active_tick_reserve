from brownie import interface
import math

def get_active_tick_bals(pool_addy):
    pool = interface.pool(pool_addy)

    sqrtPriceX96, tick = pool.slot0()[0], pool.slot0()[1]
    ts = pool.tickSpacing()
    sqrtP = sqrtPriceX96 / 2**96

    t0, t1 = interface.ERC20(pool.token0()), interface.ERC20(pool.token1())
    decimals0, decimals1 = t0.decimals(), t1.decimals()
    sym0, sym1 = t0.symbol(), t1.symbol()

    liquidity = pool.liquidity()

    x = liquidity * ( math.sqrt(1.0001 ** (tick + ts) ) - sqrtP ) / (sqrtP * math.sqrt(1.0001 ** (tick + ts) )) / 10**(decimals0)
    y = liquidity * (sqrtP - math.sqrt(1.0001 ** tick ) ) / 10**(decimals1)

    return x,y, sym0, sym1

def main():
    bal0, bal1, sym0, sym1 = get_active_tick_bals('0x4742b2760837c4b080d675c6770437cdb703c877') # wstETH/WETH

    print(f"Token0 {sym0} balance:", bal0)
    print(f"Token1 {sym1} balance:", bal1)