online_shop = {
    'keychain': 0.75,
    'tshirt': 8.50,
    'bottle': 10.00
}
keychain = online_shop['keychain']
tshirt = online_shop['tshirt']
bottle = online_shop['bottle']
choicekey = int(input('How many keychains will you be purchasing? If not purchasing keychains, enter 0.'))
choicetshirt = int(input('How many t-shirts will you be purchasing? If not purchasing t-shirts, enter 0. '))
choicebottle = int(input('How many t-shirts will you be purchasing? If not purchasing water bottles, enter 0.'))

print('You are purchasing ' + str(choicekey) + ' keychains, ' + str(choicetshirt) + ' t-shirts, and ' +
str(choicebottle) + ' water bottles.')

if choicekey > 9:
 online_shop['keychain'] = 0.65
if choicetshirt > 10:
 online_shop['tshirt'] = 8.00
if choicebottle > 10:
 online_shop['bottle'] = 8.75

keychain = online_shop['keychain']
tshirt = online_shop['tshirt']
bottle = online_shop['bottle']
print(online_shop)

totalkey = choicekey * keychain
totaltshirt = choicetshirt * tshirt
totalbottle = choicebottle * bottle
grandtotal = totalkey + totaltshirt + totalbottle
print('Keychain total: $' + str(totalkey))
print('T-shirt total: $' + str(totaltshirt))
print('Water bottle total: $' + str(totalbottle))
print('Your order total: $' + str(grandtotal))

