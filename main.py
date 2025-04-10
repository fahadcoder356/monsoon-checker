import streamlit as st

def check_monsoon():
    st.title('Monsoon Checker')
    st.write('এখানে মন্সুন চেক করার জন্য ফর্ম বা তথ্য থাকবে।')

    temparature = st.number_input("আপনার এলাকার বর্তমান তাপমাত্রা (°C) লিখুন:", step=1)

    if st.button("চেক করুন"):
        result = determine_season(temparature)
        st.success(result)

    st.markdown("---")
    st.info("💡 যতদিন যাচ্ছে, জলবায়ু পরিবর্তন হচ্ছে। \
    আর এই পরিবর্তনের সাথে মিল রেখে ঝড়-বৃষ্টি বলে কিছু আর মৌসুমে আটকে নেই — \
    গরমের দুপুরে, শীতের রাতে, বর্ষার ফাঁকে, এমনকি একদম হঠাৎ করে আকাশ গর্জে উঠে, বাতাস তেড়ে আসে, তারপর নামিয়ে দেয় এক পশলা ঝড়-বৃষ্টি — যেন প্রকৃতি এখন তার ইচ্ছেমত আচরণ করছে।")

def determine_season(temparature):
    if temparature <= 15:
        return "এখন ঠান্ডা মৌসুম। গরম কাপড় পরিধান করুন। শিশু ও বয়স্কদের যত্ন নিন।"
    elif 16 <= temparature <= 30:
        return "এখন কখনো গরম, কখনো ঠান্ডা। ভাইরাস সংক্রমণ বাড়তে পারে। সচেতন থাকুন।"
    else:
        return "এখন গ্রীষ্মকাল। পর্যাপ্ত পানি পান করুন। হালকা কাপড় পরুন।"

if __name__ == '__main__':
    check_monsoon()
