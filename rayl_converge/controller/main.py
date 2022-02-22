from odoo import http, _
import requests
import logging
_logger = logging.getLogger(__name__)


class LightBoxccSaleDevportal(http.Controller):

    # To Generate Request Token
    @http.route(['/lightboxccsaledevportal'], auth='public', type='http', website=True, methods=['POST'], csrf=False)
    def light_boxcc_sale_devportal(self, **kw):
        merchant_id = '0024991'
        merchant_user_id = 'apiuser292930'
        merchant_pin_code = 'OQ5WCEK0I8AXPCUK7319UWC3R0FOWT1RIXPMJBDKN02WQMYBYZAR6HXGQLK88MR1'
        url = 'https://api.demo.convergepay.com/hosted-payments/transaction_token'
        firstname = kw.get('ssl_first_name')
        lastname = kw.get('ssl_last_name')
        amount = kw.get('ssl_amount')
        data = {
                "ssl_merchant_id": merchant_id,
                "ssl_user_id": merchant_user_id,
                "ssl_pin": merchant_pin_code,
                "ssl_transaction_type": "CCSALE",
                "ssl_first_name": firstname,
                "ssl_last_name": lastname,
                "ssl_get_token": "Y",
                "ssl_add_token": "Y",
                "ssl_amount": amount,

        }
        session_token = requests.post(url, json=data)
        _logger.info(session_token.text)
        return session_token.text

    @http.route(['/lightboxccaddrecurringdevportal'], auth='public', type='http', website=True, methods=['POST'], csrf=False)
    def submit(self, **kw):
        merchant_id = '0024991'
        merchant_user_id = 'apiuser292930'
        merchant_pin_code = 'OQ5WCEK0I8AXPCUK7319UWC3R0FOWT1RIXPMJBDKN02WQMYBYZAR6HXGQLK88MR1'
        url = 'https://api.demo.convergepay.com/hosted-payments/transaction_token'
        _logger.info(kw)
        firstname = kw.get('ssl_first_name')
        lastname = kw.get('ssl_last_name')
        amount = kw.get('ssl_amount')
        card_number = kw.get('ssl_card_number')
        exp_date = kw.get('ssl_exp_date')
        txn_id = kw.get('ssl_txn_id')
        data = {
            "ssl_merchant_id": merchant_id,
            "ssl_user_id": merchant_user_id,
            "ssl_pin": merchant_pin_code,
            "ssl_transaction_type": "ccaddrecurring",
            "ssl_first_name": firstname,
            "ssl_last_name": lastname,
            "ssl_get_token": "Y",
            "ssl_add_token": "Y",
            "ssl_amount": amount,
            "ssl_card_number":card_number,
            "ssl_exp_date":exp_date,
            "ssl_txn_id":txn_id,
            "ssl_next_payment_date": "08/04/2022",
            "ssl_billing_cycle": "MONTHLY",
            "ssl_end_of_month": "Y",

        }
        session_token = requests.post(url, json=data)
        _logger.info(session_token.text)
        return session_token.text

