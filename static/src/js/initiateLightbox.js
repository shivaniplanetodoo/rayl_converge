function initiateLightbox(){

      var tokenRequest = {
                ssl_first_name: document.getElementById('partner').value,
                ssl_last_name: document.getElementById('partner').value,
                ssl_amount: document.getElementById('amount').value,
                csrf_token: odoo.csrf_token
      };
      $.post("/lightboxccsaledevportal", tokenRequest, function (data) {
        //document.getElementById('token').value = data;
        console.log(data);
        transactionToken = data;
        if(transactionToken){
            return openLightbox(transactionToken);
        }
    });

      return false;
}

function openLightbox(transactionToken) {
    //alert(transactionToken);
    var paymentFields = {
        ssl_txn_auth_token: transactionToken
    };
    console.log(paymentFields);
    var callback = {
        onError: function (error) {
            showResult("error", error);
        },
        onCancelled: function () {
            showResult("cancelled", "");
        },
        onDeclined: function (response) {
            console.log(response);
            showResult("declined", JSON.stringify(response, null, '\t'));
        },
        onApproval: function (response) {
            console.log(response);
            showResult("approval", JSON.stringify(response, null, '\t'));
            $.post("/lightboxccaddrecurringdevportal", response, function (data) {
        //document.getElementById('token').value = data;
            console.log(data);
    });
        }
    };
    PayWithConverge.open(paymentFields, callback);
    return false;
}

function showResult(status, msg) {
            //document.getElementById('txn_status').innerHTML = "<b>" + status + "</b>";
            //document.getElementById('txn_response').innerHTML = msg;
            console.log("status", status)
            console.log("msg", msg)
        }

function checkPay(){
    var pay=document.getElementById('elavon_pay_now');
    pay.addEventListener('click', function (event) {
        initiateLightbox();
    });
}
