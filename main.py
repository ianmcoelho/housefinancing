import math


def juros_aa_to_am(juros_aa):
    return (math.pow(1.0 + juros_aa / 100.0, 1 / 12.0) - 1) * 100


FGTS = 50000
SELIC = 120000
valor_imovel = 400000
aluguel = 1320.05
parcelas = 360

valor_financiado = valor_imovel - (SELIC + FGTS)

selic_aa = 10.5
selic_am = juros_aa_to_am(selic_aa)

fgts_aa = 3
fgts_am = juros_aa_to_am(fgts_aa)

taxa_juros_aa = 10.3
taxa_juros_am = juros_aa_to_am(taxa_juros_aa)

amortizacao = valor_financiado / parcelas

print "financiado | juros aa | juros am | parcelas | amortizacao | selic aa | selic am | fgts aa | fgts am"
print "{:10d} | {:7.2f}% | {:7.2f}% | {:8d} | {:11.2f} | {:8.2f} | {:8.2f} | {:7.2f} | {:7.2f}".format(valor_financiado, taxa_juros_aa, taxa_juros_am, parcelas, amortizacao, selic_aa, selic_am, fgts_aa, fgts_am)

print "                 apartamento financiado                                                           |                                 aluguel                                                 "
print "parc | saldo devedor |   juros | saldo atualizado | prestacao |    imovel |      FGTS |     total |  aporte | juros selic | acumulado selic | juros fgts | acumulado fgts | total acumulado "

fgts_mensal = 1000.0

saldo_devedor = valor_financiado
imovel = SELIC + FGTS
fgts_imovel = 0.0

acumulado_selic = SELIC
acumulado_fgts = FGTS
for i in range(1, parcelas + 1):
    juros = saldo_devedor * taxa_juros_am/100
    saldo_atualizado = saldo_devedor + juros
    prestacao = saldo_atualizado - saldo_devedor + amortizacao
    imovel += amortizacao
    fgts_imovel = fgts_imovel + (fgts_imovel * fgts_am/100) + fgts_mensal
    total_imovel = imovel + fgts_imovel

    juros_selic = acumulado_selic * selic_am / 100
    aporte_selic = prestacao - aluguel
    if(aporte_selic < 0):
        aporte_selic = 0
    acumulado_selic += juros_selic + aporte_selic

    juros_fgts = acumulado_fgts * fgts_am/100
    aporte_fgts = fgts_mensal
    acumulado_fgts += juros_fgts + aporte_fgts

    total_acumulado = acumulado_selic + acumulado_fgts

    # "parc | saldo devedor |   juros | saldo atualizado | prestacao | imovel |     FGTS |   total |  aporte | juros selic | acumulado selic | juros fgts | acumulado fgts | total acumulado "
    #        4   |     13   |    7    |    16    |    9    |   9     |   8     |    8    |   7     |    11    |    15    |   10     |    14    |      15         "
    # "    parc  |     sd   |   juros |     sa   | prestac | imovel  |  fgts   |   total | aporte  |   jSelic | aSelic   | jFGTS    | aFGTS    | total acumulado "
    print "{:4d} | {:13.2f} | {:7.2f} | {:16.2f} | {:9.2f} | {:9.2f} | {:9.2f} | {:9.2f} | {:7.2f} | {:11.2f} | {:15.2f} | {:10.2f} | {:14.2f} | {:15.2f}" \
        .format(i, saldo_devedor, juros, saldo_atualizado, prestacao, imovel, fgts_imovel, total_imovel, aporte_selic, juros_selic, acumulado_selic, juros_fgts, acumulado_fgts, total_acumulado)

    saldo_devedor = saldo_atualizado - prestacao

print "parc | saldo devedor |   juros | saldo atualizado | prestacao |    imovel |      FGTS |     total |  aporte | juros selic | acumulado selic | juros fgts | acumulado fgts | total acumulado "
print "                 apartamento financiado                                                           |                                 aluguel                                                 "
