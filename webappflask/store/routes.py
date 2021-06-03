from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import login_required, current_user
from webappflask.models import Item
from webappflask.store.forms import PurchaseItemForm

store = Blueprint('store', __name__)


@store.route('/store', methods=['GET', 'POST'])
@login_required
def shelf():
    purchase_form = PurchaseItemForm()
    if request.method == "POST":
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$", category='success')
            else:
                flash(f"Unfortunately, you don't have enough money to purchase {p_item_object.name}!", category='danger')

        return redirect(url_for('store.shelf'))

    if request.method == "GET":
        items = Item.query.filter_by(user_id=None)
        owned_items = Item.query.filter_by(user_id=current_user.id)
        return render_template('store.html', items=items, purchase_form=purchase_form, owned_items=owned_items)
