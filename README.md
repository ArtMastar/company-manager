# company-manager

FILE STRUCTURE
company_manager/
├── manage.py
├── company_manager/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── accounts/
│           ├── login.html
│           └── dashboard.html
├── inventory/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── inventory/
│           ├── inventory_list.html
│           ├── inventory_form.html
│           └── inventory_confirm_delete.html
├── orders/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── orders/
│           ├── order_list.html
│           ├── order_detail.html
│           ├── order_form.html
│           └── order_confirm_delete.html
├── payments/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── payments/
│           ├── payment_list.html
│           └── payment_form.html
├── invoices/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── invoices/
│           ├── invoice_list.html
│           ├── invoice_detail.html
│           ├── invoice_form.html
│           └── invoice_confirm_delete.html
└── analytics/
    ├── __init__.py
    ├── apps.py
    ├── urls.py
    ├── views.py
    └── templates/
           └── analytics/
                   └── dashboard.html
                   
And a global base template in (for example) a “templates” folder (or in each app as needed):

templates/
└── base.html
                                                    