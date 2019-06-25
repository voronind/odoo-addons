# -*- coding: utf-8 -*-

from odoo import models, api, tools


class ViewModel(models.AbstractModel):
    _abstract = False

    def _select(self):
        raise NotImplementedError

    def _from(self):
        return ''

    def _group_by(self):
        return ''

    def _query(self):
        return ' '.join([
            self._select(),
            self._from(),
            self._group_by(),
        ])

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)

        self._cr.execute(
            'create view {name} as ({query})'.format(
                name=self._table,
                query=self._query(),
                )
        )
