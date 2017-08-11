from django.db import models
# Neste arquivo ficam escritas todas as models relativas ao produto


class Produto(models.Model):
    prod_codigo = models.BigIntegerField(db_column='prod_codigo', primary_key=True)
    prod_alias = models.CharField(db_column='prod_alias', max_length=50, null=False)
    prod_descricao = models.CharField(db_column='prod_descricao', max_length=255, null=False)
    prod_valor_venda = models.DecimalField(db_column='prod_valor_venda', max_digits=13, decimal_places=2)
    prod_valor_compra = models.DecimalField(db_column='prod_valor_compra', max_digits=13, decimal_places=2)
    prod_peso_b = models.DecimalField(db_column='prod_peso_b', max_digits=13, decimal_places=2)
    prod_peso_l = models.DecimalField(db_column='prod_peso_l', max_digits=13, decimal_places=2)

    class Meta:
        db_table = 'produto'
        managed = True
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.prod_alias + ' - ' + self.prod_descricao
