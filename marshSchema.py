import warlock

addressSchema ={
  "$schema": "http://json-schema.org/draft-04/schema#",
  "description": "An address record",
  "type": "object",
  "properties": {
    "id": {
      "description": "UUID"

    },
    "addressLine1": {
      "description": "The first line of this address",
      "type": "string"
    },
    "addressLine2": {
      "description": "The second line of this address",
      "type": "string"
    },
    "city": {
      "description": "The city for this address",
      "type": "string"
    },
    "stateRegion": {
      "description": "The state or region for this address",
      "type": "string"
    },
    "zipCode": {
      "description": "The zip code for this address",
      "type": "string"
    },
    "country": {
      "description": "The country for this address",
      "type": "string"
    },
    "isPrimary": {
      "description": "Used to set this address as primary for the contact",
      "type": "boolean"
    },
    "categories": {
      "id": "categories",
      "description": "The list of categories for this organization address",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "language": {
      "description": "The language for this organization address",
      "type": "string"
    },
    "metadata": {
      "type": "object",
      "$ref": "../../../raml-util/schemas/metadata.schema",
      "readonly": True
    }
  },
  "additionalProperties": False
}

organizationSchema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "description": "The record of an organization",
  "type": "object",
  "properties": {
    "id": {
      "description": "The unique UUID for this organization"

    },
    "name": {
      "description": "The name of this organization",
      "type": "string"
    },
    "code": {
      "description": "The code for this organization",
      "type": "string"
    },
    "description": {
      "description": "The description for this organization",
      "type": "string"
    },
    "status": {
      "description": "The status of this organization",
      "type": "string",
      "enum": [
        "Active",
        "Inactive",
        "Pending"
      ]
    },
    "language": {
      "description": "The language for this organization",
      "type": "string"
    },
    "aliases": {
      "id": "aliases",
      "description": "The list of aliases for this organization",
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "addresses": {
      "id": "addresses",
      "description": "The list of addresses for this organization",
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "phoneNumbers": {
      "id": "phoneNumbers",
      "description": "The list of phone numbers for this organization",
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "emails": {
      "id": "emailAddresses",
      "description": "The list of emails for this organization",
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "urls": {
      "id": "urls",
      "description": "The list of URLs for this organization",
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "contacts": {
      "id": "contact",
      "description": "An array of contact record IDs",
      "type": "array",
      "items": {
        "description": "UUID of a contact record"
      }
    },
    "agreements": {
      "id": "agreement",
      "description": "The the list of agreements for this organization",
      "type": "array",
      "items": {
        "type": "object",
        "$ref": "agreement.json"
      }
    },
    "erpCode": {
      "description": "The ERP code for this organization",
      "type": "string"
    },
    "paymentMethod": {
      "description": "The payment method for this organization",
      "type": "string"
    },
    "accessProvider": {
      "description": "The access provider for this organization",
      "type": "boolean"
    },
    "governmental": {
      "description": "The setting to mark this organization as governmental",
      "type": "boolean"
    },
    "licensor": {
      "description": "The setting to mark this organization as a licensor",
      "type": "boolean"
    },
    "materialSupplier": {
      "description": "The setting to mark this organization as a material supplier",
      "type": "boolean"
    },
    "vendorCurrencies": {
      "id": "vendorCurrencies",
      "description": "The list of currencies used by this organization",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "claimingInterval": {
      "description": "The claim interval for this organization",
      "type": "integer"
    },
    "discountPercent": {
      "description": "The discount percentage for this organization",
      "type": "number"
    },
    "expectedActivationInterval": {
      "description": "The expected activation interval (in days) for this organization",
      "type": "integer"
    },
    "expectedInvoiceInterval": {
      "description": "The expected invoice interval (in days) for this organization",
      "type": "integer"
    },
    "renewalActivationInterval": {
      "description": "The revewal activation interval (in days) for this organization",
      "type": "integer"
    },
    "subscriptionInterval": {
      "description": "The subscription interval (in days) for this organization",
      "type": "integer"
    },
    "expectedReceiptInterval": {
      "description": "The receipt interval (in days) for this organization",
      "type": "integer"
    },
    "taxId": {
      "description": "The tax ID for this organization",
      "type": "string"
    },
    "liableForVat": {
      "description": "The setting to mark this organization liable to collect VAT",
      "type": "boolean"
    },
    "taxPercentage": {
      "description": "The tax percentage value for this organization",
      "type": "number"
    },
    "edi": {
      "description": "The EDI object for this organization (only applicable when isVendor is true)",
      "type": "object",
      "properties": {
        "vendorEdiCode": {
          "description": "The organization code for this EDI",
          "type": "string"
        },
        "vendorEdiType": {
          "description": "The organization type for this EDI",
          "type": "string",
          "enum": [
            "014/EAN",
            "31B/US-SAN",
            "091/Vendor-assigned",
            "092/Customer-assigned"
          ]
        },
        "libEdiCode": {
          "description": "The library code for this EDI",
          "type": "string"
        },
        "libEdiType": {
          "description": "The library type for this EDI",
          "type": "string",
          "enum": [
            "014/EAN",
            "31B/US-SAN",
            "091/Vendor-assigned",
            "092/Customer-assigned"
          ]
        },
        "prorateTax": {
          "description": "The setting to prorate tax for this EDI",
          "type": "boolean"
        },
        "prorateFees": {
          "description": "The setting to prorate fees for this EDI",
          "type": "boolean"
        },
        "ediNamingConvention": {
          "description": "The naming convention for this EDI",
          "type": "string"
        },
        "sendAcctNum": {
          "description": "The setting to send the account number for this EDI",
          "type": "boolean"
        },
        "supportOrder": {
          "description": "The setting to support order for this EDI",
          "type": "boolean"
        },
        "supportInvoice": {
          "description": "The setting to support invoice for this EDI",
          "type": "boolean"
        },
        "notes": {
          "description": "The notes for this EDI",
          "type": "string"
        },
        "ediFtp": {
          "description": "The FTP object for this EDI",
          "type": "object",
          "properties": {
            "ftpFormat": {
              "description": "The FTP format for this EDI",
              "type": "string",
              "enum": [
                "SFTP",
                "FTP"
              ]
            },
            "serverAddress": {
              "description": "The server address for this EDI",
              "type": ["string", "null"],
              "pattern": "^$|(([Hh][Tt][Tt][Pp]|[Ff][Tt][Pp])([Ss])?://.+$)"
            },
            "username": {
              "description": "The login username for this EDI",
              "type": "string"
            },
            "password": {
              "description": "The login password for this EDI",
              "type": "string"
            },
            "ftpMode": {
              "description": "The FTP mode for this EDI",
              "type": "string",
              "enum": [
                "ASCII",
                "Binary"
              ]
            },
            "ftpConnMode": {
              "description": "The FTP connection mode for this EDI",
              "type": "string",
              "enum": [
                "Active",
                "Passive"
              ]
            },
            "ftpPort": {
              "description": "The port for this EDI",
              "type": "integer"
            },
            "orderDirectory": {
              "description": "The order directory for this EDI",
              "type": "string"
            },
            "invoiceDirectory": {
              "description": "The invoice directory for this EDI",
              "type": "string"
            },
            "notes": {
              "description": "The notes for this EDI",
              "type": "string"
            }
          }
        },
        "ediJob": {
          "description": "The job object for this EDI",
          "type": "object",
          "properties": {
            "scheduleEdi": {
              "description": "Activate the schedule for this EDI job",
              "type": "boolean"
            },
            "schedulingDate": {
              "description": "The date (MM/DD/YYYY) for this EDI job to start running",
              "type": ["string", "null"],
              "format": "date-time"
            },
            "time": {
              "description": "The time (h:mm A) for this EDI job",
              "type": ["string", "null"],
              "format": "time"
            },
            "isMonday": {
              "description": "The setting to run this EDI job on Mondays",
              "type": "boolean"
            },
            "isTuesday": {
              "description": "The setting to run this EDI job on Tuesdays",
              "type": "boolean"
            },
            "isWednesday": {
              "description": "The setting to run this EDI job on Wednesdays",
              "type": "boolean"
            },
            "isThursday": {
              "description": "The setting to run this EDI job on Thursdays",
              "type": "boolean"
            },
            "isFriday": {
              "description": "The setting to run this EDI job on Fridays",
              "type": "boolean"
            },
            "isSaturday": {
              "description": "The setting to run this EDI job on Saturdays",
              "type": "boolean"
            },
            "isSunday": {
              "description": "The setting to run this EDI job on Sundays",
              "type": "boolean"
            },
            "sendToEmails": {
              "description": "The comma delimited list of email addresses to notify when this EDI job runs",
              "type": "string"
            },
            "notifyAllEdi": {
              "description": "The setting to notify all receivers when this EDI job runs",
              "type": "boolean"
            },
            "notifyInvoiceOnly": {
              "description": "The setting to notify only the invoice receiver when this EDI job runs",
              "type": "boolean"
            },
            "notifyErrorOnly": {
              "description": "The setting to notiry on the error receiver when this EDI job runs",
              "type": "boolean"
            },
            "schedulingNotes": {
              "description": "The schedule notes for this EDI job",
              "type": "string"
            }
          }
        }
      }
    },
    "interfaces": {
      "id": "interfaces",
      "description": "The list of interfaces assigned to this organization",
      "type": "array",
      "items": {
        "description": "UUID of an interface record"

      }
    },
    "accounts": {
      "id": "accounts",
      "description": "The list of accounts for this organization",
      "type": "array",
      "items": {
        "type": "object",
        "$ref": "account.json"
      }
    },
    "isVendor": {
      "id": "isVendor",
      "description": "Used to indicate that this organization is also a vendor",
      "type": "boolean",
      "default": False
    },
    "sanCode": {
      "description": "The SAN code for this organization address",
      "type": "string"
    },
    "changelogs": {
      "id": "changelogs",
      "description": "The list of changes applied to this organization",
      "type": "array",
      "items": {
        "type": "object",
        "$ref": "changelog.json"
      }
    },
    "tags": {
      "type": "object",
      "description": "arbitrary tags associated with this organization",
      "$ref": "../../../raml-util/schemas/tags.schema"
    },
    "metadata": {
      "type": "object",
      "$ref": "../../../raml-util/schemas/metadata.schema",
      "readonly": True
    }
  },
  "additionalProperties": False,
  "required": [
    "name",
    "status",
    "code"
  ]
}

emailSchema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "description": "An email record",
  "type": "object",
  "properties": {
    "id": {
      "description": "The unique id of this email",
      "$ref": "../../common/schemas/uuid.json"
    },
    "value": {
      "description": "The value for this email",
      "type": "string"
    },
    "description": {
      "description": "The description for this email",
      "type": "string"
    },
    "isPrimary": {
      "description": "Used to set this email as primary for the contact",
      "type": "boolean"
    },
    "categories": {
      "id": "categories",
      "description": "The list of categories for this organization email",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "language": {
      "description": "The language for this organization email",
      "type": "string"
    },
    "metadata": {
      "type": "object",
      "$ref": "../../../raml-util/schemas/metadata.schema",
      "readonly": True
    }
  },
  "additionalProperties": False,
  "required": [
    "value"
  ]
}

urlSchema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "description": "A URL record",
  "type": "object",
  "properties": {
    "id": {
      "description": "The unique id of this url",
      "$ref": "../../common/schemas/uuid.json"
    },
    "value": {
      "description": "The value for this URL",
      "type": "string",
      "pattern": "^$|(([Hh][Tt][Tt][Pp]|[Ff][Tt][Pp])([Ss])?://.+$)"
    },
    "description": {
      "description": "The description for this URL",
      "type": "string"
    },
    "language": {
      "description": "The language for this organization URL",
      "type": "string"
    },
    "isPrimary": {
      "description": "Used to set this url as primary for the contact",
      "type": "boolean"
    },
    "categories": {
      "id": "categories",
      "description": "The list of categories for this organization URL",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "notes": {
      "description": "The notes for this organization URL",
      "type": "string"
    },
    "metadata": {
      "type": "object",
      "$ref": "../../../raml-util/schemas/metadata.schema",
      "readonly": True
    }
  },
  "additionalProperties": False,
  "required": [
    "value"
  ]
}

phoneSchema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "description": "A phone number record",
  "type": "object",
  "properties": {
    "id": {
      "description": "UUID",
      "$ref": "../../common/schemas/uuid.json"
    },
    "phoneNumber": {
      "description": "The entire sequence of digits for this phone number",
      "type": "string"
    },
    "categories": {
      "id": "categories",
      "description": "The list of categories for this organization phone",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "type": {
      "description": "The type of this phone number",
      "type": "string",
       "enum": [
         "Office",
         "Mobile",
         "Fax",
         "Other"
      ]
    },
    "isPrimary": {
      "description": "Used to set this phone number as primary for the contact",
      "type": "boolean"
    },
    "language": {
      "description": "The language for this organization phone",
      "type": "string"
    },
    "metadata": {
      "type": "object",
      "$ref": "../../../raml-util/schemas/metadata.schema",
      "readonly": True
    }
  },
  "additionalProperties": False,
  "required": [
    "phoneNumber"
  ]
}

aliasSchema =  {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "description": "An organization alias",
  "type": "object",
  "properties": {
    "value": {
      "description": "The unique name of this alias",
      "type": "string"
    },
    "description": {
      "description": "The description of this alias",
      "type": "string"
    }
  },
  "additionalProperties": False,
  "required": [
    "value"
  ]
}

interfaceSchema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "description": "An interface record",
  "type": "object",
  "properties": {
    "id": {
      "description": "The unique id of this interface",
      "$ref": "../../common/schemas/uuid.json"
    },
    "name": {
      "description": "The name of this interface",
      "type": "string"
    },
    "uri": {
      "description": "The URI of this interface",
      "type": "string"
    },
    "notes": {
      "description": "The notes for this interface",
      "type": "string"
    },
    "available": {
      "description": "The availability setting for this interface",
      "type": "boolean"
    },
    "deliveryMethod": {
      "description": "The delivery method for this interface",
      "type": "string",
      "enum": [
        "Online",
        "FTP",
        "Email",
        "Other"
      ]
    },
    "statisticsFormat": {
      "description": "The format of the statistics for this interface",
      "type": "string"
    },
    "locallyStored": {
      "description": "The locally stored location of this interface",
      "type": "string"
    },
    "onlineLocation": {
      "description": "The online location for this interface",
      "type": "string"
    },
    "statisticsNotes": {
      "description": "The notes regarding the statistics for this interface",
      "type": "string"
    },
    "type": {
      "description": "Interface types",
      "type": "array",
      "items": {
        "type": "object",
        "$ref": "interface_type.json"
      }
    },
    "metadata": {
      "type": "object",
      "$ref": "../../../raml-util/schemas/metadata.schema",
      "readonly": True
    }
  },
  "additionalProperties": False
}

contactSchema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "description": "A contact record",
  "type": "object",
  "properties": {
    "id": {
      "description": "The unique id of this contact",
      "$ref": "../../common/schemas/uuid.json"
    },
    "prefix": {
      "description": "The prefix for this contact person",
      "type": "string"
    },
    "firstName": {
      "description": "The first name of this contact person",
      "type": "string"
    },
    "lastName": {
      "description": "The last name of this contact person",
      "type": "string"
    },
    "language": {
      "description": "The preferred language for this contact person",
      "type": "string"
    },
    "notes": {
      "description": "The notes for this contact person",
      "type": "string"
    },
    "phoneNumbers": {
      "id": "phoneNumbers",
      "description": "The list of phone numbers for this contact person",
      "type": "array",
      "items": {
        "type": "object",
        "$ref": "phone_number.json"
      }
    },
    "emails": {
      "id": "emailAddresses",
      "description": "The list of emails for this contact person",
      "type": "array",
      "items": {
        "type": "object",
        "$ref": "email.json"
      }
    },
    "addresses": {
      "id": "addresses",
      "description": "The list of addresses for this contact person",
      "type": "array",
      "items": {
        "type": "object",
        "$ref": "address.json"
      }
    },
    "urls": {
      "id": "urls",
      "description": "The list of URLs for this contact person",
      "type": "array",
      "items": {
        "type": "object",
        "$ref": "url.json"
      }
    },
    "categories": {
      "id": "contactCategory",
      "description": "The list of contact categories associated with this organization contact person",
      "type": "array",
      "items": {
        "description": "UUID of the contact category",
        "$ref": "../../common/schemas/uuid.json"
      }
    },
    "inactive": {
      "description": "Used to indicate that a contact is no longer active",
      "type": "boolean",
      "default": False
    },
    "metadata": {
      "type": "object",
      "$ref": "../../../raml-util/schemas/metadata.schema",
      "readonly": True
    }
  },
  "additionalProperties": False,
  "required": [
    "firstName",
    "lastName"
  ]
}

emailRecord = warlock.model_factory(emailSchema)
phoneRecord = warlock.model_factory(phoneSchema)
addressRecord = warlock.model_factory(addressSchema)
organizationRecord = warlock.model_factory(organizationSchema)
urlRecord = warlock.model_factory(urlSchema)
aliasRecord = warlock.model_factory(aliasSchema)
interfaceRecord = warlock.model_factory(interfaceSchema)
contactRecord = warlock.model_factory(contactSchema)
