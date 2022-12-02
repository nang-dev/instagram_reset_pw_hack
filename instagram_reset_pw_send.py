import os
import json

print("\nEnter Username to make instagram send Reset Password via SMS:")
username = input()

command = "curl -H 'x-ig-app-locale: en_US' -H 'x-ig-device-locale: en_US' -H 'x-ig-mapped-locale: en_US' -H 'x-pigeon-session-id: UFS-75d22c77-e210-4f47-8964-1e956d54cb41-2' -H 'x-pigeon-rawclienttime: 1656150704.978' -H 'x-ig-bandwidth-speed-kbps: -1.000' -H 'x-ig-bandwidth-totalbytes-b: 0' -H 'x-ig-bandwidth-totaltime-ms: 0' -H 'x-bloks-version-id: 8dab28e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07' -H 'x-ig-www-claim: 0' -H 'x-bloks-is-layout-rtl: false' -H 'x-ig-device-id: 08066955-5663-4f45-a1cb-dad527159bbe' -H 'x-ig-family-device-id: 7c6340c6-2719-44e1-8ff8-0fed8de85300' -H 'x-ig-android-id: android-535de087d814bc86' -H 'x-ig-timezone-offset: -14400' -H 'x-ig-nav-chain: AD2:password_lookup:1:button::,9jv:user_password_recovery:2:button::,ADf:landing_facebook:3:button::,AD1:login_landing:4:button::,AD1:login_landing:5:warm_start::,AD2:password_lookup:6:button::,AD2:password_lookup:7:warm_start::,9jv:user_password_recovery:8:button::' -H 'x-fb-connection-type: WIFI' -H 'x-ig-connection-type: WIFI' -H 'x-ig-capabilities: 3brTv10=' -H 'x-ig-app-id: 567067343352427' -H 'priority: u=3' -H 'user-agent: Instagram 237.0.0.14.102 Android (28/9; 160dpi; 590x720; innotek GmbH/Android-x86; VirtualBox; x86_64; android_x86_64; en_US; 373310563)' -H 'accept-language: en-US' -H 'x-mid: YrNv0QABAAH7ISic1KPmuSCost6e' -H 'ig-intended-user-id: 0' -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' --compressed -H 'x-fb-http-engine: Liger' -H 'x-fb-client-ip: True' -H 'x-fb-server-cluster: True' -X POST https://i.instagram.com/api/v1/users/lookup_phone/ -d signed_body=SIGNATURE.%7B%22supports_sms_code%22%3A%22true%22%2C%22guid%22%3A%2208066955-5663-4f45-a1cb-dad527159bbe%22%2C%22device_id%22%3A%22android-535de087d814bc86%22%2C%22query%22%3A%22" + username + "%22%2C%22android_build_type%22%3A%22release%22%2C%22waterfall_id%22%3A%226cade24c-f0f9-475e-9dbd-880dd3703621%22%2C%22use_whatsapp%22%3A%22false%22%7D"

# result = subprocess.call(command, shell=True)

output_stream = os.popen(command)
result = output_stream.read()
js = json.loads(result)
status = js['status']

print("Response: ", result)

if status == "fail":
    print("Failed: ", js['message'])

else:   
    print("\nSuccess, reset password text sent!")