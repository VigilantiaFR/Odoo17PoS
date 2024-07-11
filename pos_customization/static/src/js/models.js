/** @odoo-module **/
import { Order, Orderline, Product } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";



patch(Order.prototype, {
    // Override
    setup() {
        super.setup(...arguments);
    },
    export_for_printing() {
        var json = super.export_for_printing(...arguments);
        json['is_take_away'] = this.is_take_away || false;
        return json;
    },
    export_as_JSON () {
        var json = super.export_as_JSON(...arguments);
        json['is_take_away'] = this.is_take_away || false;
        return json;
    },
});

