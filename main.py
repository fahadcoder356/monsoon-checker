import streamlit as st

def determine_season(temperature):
    if temperature <= 15:
        return "এখন ঠান্ডা মৌসুম। আপনারা অবশ্যই গরম কাপড় পরিধান করবেন।"
    elif 16 <= temperature <= 30:
        return "এখন মিশ্র অনুভূতির মধ্যে থাকা সময়। ভাইরাস ব্যাকটেরিয়ার সংক্রমণ বাড়বে।"
    else:
        return "এখন গ্রীষ্মকাল। পর্যাপ্ত পানি পান করুন এবং ঢিলেঢালা পোশাক পরুন।"

# Streamlit UI
st.title('Monsoon Checker')
st.write("এখানে মন্সুন চেক করার জন্য তথ্য থাকবে।")

temperature = st.slider("আপনার তাপমাত্রা (°C) নির্বাচন করুন:", min_value=-10, max_value=50)

if st.button("Check Season"):
    season = determine_season(temperature)
    st.write(season)
