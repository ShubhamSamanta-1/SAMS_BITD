{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cfc854bb",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "(unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \\UXXXXXXXX escape (<ipython-input-2-90e1cb774ac0>, line 33)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-2-90e1cb774ac0>\"\u001b[1;36m, line \u001b[1;32m33\u001b[0m\n\u001b[1;33m    f = open(\"C:\\Users\\vaibh\\Downloads\\Attendance-System--main\\Attendance-System--main\\Project attendance\\Attendance\\Attendance_31-03-2022.csv\", \"r\")\u001b[0m\n\u001b[1;37m            ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \\UXXXXXXXX escape\n"
     ]
    }
   ],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.chrome.options import Options\n",
    "from selenium.webdriver.support.ui import WebDriverWait\n",
    "from selenium.webdriver.support import expected_conditions as EC\n",
    "from selenium.webdriver.common.by import By\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "from time import sleep\n",
    "from urllib.parse import quote\n",
    "import os\n",
    "\n",
    "def send():\n",
    "        options = Options()\n",
    "        options.add_experimental_option(\"excludeSwitches\", [\"enable-logging\"])\n",
    "        options.add_argument(\"--profile-directory=Default\")\n",
    "        options.add_argument(\"--user-data-dir=/var/tmp/chrome_user_data\")\n",
    "\n",
    "        os.system(\"\")\n",
    "        os.environ[\"WDM_LOG_LEVEL\"] = \"0\"\n",
    "        class style():\n",
    "            BLACK = '\\033[30m'\n",
    "            RED = '\\033[31m'\n",
    "            GREEN = '\\033[32m'\n",
    "            YELLOW = '\\033[33m'\n",
    "            BLUE = '\\033[34m'\n",
    "            MAGENTA = '\\033[35m'\n",
    "            CYAN = '\\033[36m'\n",
    "            WHITE = '\\033[37m'\n",
    "            UNDERLINE = '\\033[4m'\n",
    "            RESET = '\\033[0m'\n",
    "\n",
    "\n",
    "\n",
    "        f = open(\"C:\\Users\\vaibh\\Downloads\\Attendance-System--main\\Attendance-System--main\\Project attendance\\Attendance\\Attendance_31-03-2022.csv\", \"r\")\n",
    "        message = f.read()\n",
    "        f.close()\n",
    "\n",
    "        print(style.YELLOW + '\\nThis is your message-')\n",
    "        print(style.GREEN + message)\n",
    "        print(\"\\n\" + style.RESET)\n",
    "        message = quote(message)\n",
    "\n",
    "        numbers = []\n",
    "        f = open(\"numbers.txt\", \"r\")\n",
    "        for line in f.read().splitlines():\n",
    "            if line.strip() != \"\":\n",
    "                numbers.append(line.strip())\n",
    "        f.close()\n",
    "        total_number=len(numbers)\n",
    "        print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)\n",
    "        delay = 30\n",
    "\n",
    "        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)\n",
    "        print('Once your browser opens up sign in to web whatsapp')\n",
    "        driver.get('https://web.whatsapp.com')\n",
    "        input(style.MAGENTA + \"AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER...\" + style.RESET)\n",
    "        for idx, number in enumerate(numbers):\n",
    "            number = number.strip()\n",
    "            if number == \"\":\n",
    "                continue\n",
    "            print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), total_number, number) + style.RESET)\n",
    "            try:\n",
    "                url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message\n",
    "                sent = False\n",
    "                for i in range(3):\n",
    "                    if not sent:\n",
    "                        driver.get(url)\n",
    "                        try:\n",
    "                            click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, \"//button[@class='_4sWnG']\")))\n",
    "                        except Exception as e:\n",
    "                            print(style.RED + f\"\\nFailed to send message to: {number}, retry ({i+1}/3)\")\n",
    "                            print(\"Make sure your phone and computer is connected to the internet.\")\n",
    "                            print(\"If there is an alert, please dismiss it.\" + style.RESET)\n",
    "                        else:\n",
    "                            sleep(1)\n",
    "                            click_btn.click()\n",
    "                            sent=True\n",
    "                            sleep(3)\n",
    "                            print(style.GREEN + 'Message sent to: ' + number + style.RESET)\n",
    "            except Exception as e:\n",
    "                print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)\n",
    "        driver.close()\n",
    "        \n",
    "send()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e953bb73",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
