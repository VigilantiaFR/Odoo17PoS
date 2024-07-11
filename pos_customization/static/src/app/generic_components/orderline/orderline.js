/** @odoo-module */

import { useService } from "@web/core/utils/hooks";
import { Orderline } from "@point_of_sale/app/generic_components/orderline/orderline";
import { patch } from "@web/core/utils/patch";
import { usePos } from "@point_of_sale/app/store/pos_hook";


patch(Orderline.prototype, {
    // Override
    setup() {
        var self = this
        super.setup(...arguments);
        this.pos = usePos();
    },
    get currentOrderLine() {
        return this.props.slots.default.__ctx.line;
    },
    get_product_price(line) {
        var self = this
        var currentLine = this.currentOrderLine;
        var total_price = 0;
        if(currentLine.comboLines && currentLine.comboLines.length) {
            currentLine.comboLines.map(function(childLines){
                total_price += childLines.get_price_with_tax();
            });
            return self.pos.env.utils.formatCurrency(total_price)
        }
        return line.price
    }

 });
