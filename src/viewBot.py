# -*- coding: utf-8 -*-
"""
Summary viewBot.

Bot that generates views on a YouTube video by simulating human interaction with the video.

"""

import argparse
from fake_useragent import UserAgent
from multiprocessing import freeze_support
import pyautogui
import random
from selenium import webdriver
from time import sleep
import subprocess
import warnings
from webdriver_manager.chrome import ChromeDriverManager


def establish_args():
    """
    Summary establish_args.

    Parse the user-entered command-line args

    Returns
    -------
    args : iterable
        Iterable object containing all the entered command-line args.

    """
    parser = argparse.ArgumentParser(description="Search for a video on YouTube and have bot watch it for you")
    parser.add_argument('-s', '--search_string', help='phrase to search on YouTube')
    parser.add_argument('-n', '--num_runs', help='number of times to run the viewBot in total')
    parser.add_argument('--max', help='max amount of seconds to watch video for')
    parser.add_argument('--min', help='min amount of seconds to watch video for')
    args = parser.parse_args()
    return args


def establish_proxy(commands):
    """
    Summary establish_proxy.

    Use nordVPN to establish proxy IP address

    Parameters
    ----------
    commands : list
        List of command line args used to establish a proxy.

    Returns
    -------
    None.

    """
    print('\n[~] Connecting to proxy. Please wait ...\n')
    command = random.choice(commands)
    country = command.split(" ")[-1].split('"')[1]
    subprocess.run(command)
    sleep(5)
    print(f'\n[~] Connected to {country}')


def get_commands():
    """
    Summary get_commands.

    Used to load the commands from 'proxy_list.txt' into a list

    Returns
    -------
    commands : list
        List of command line args used to establish a proxy.

    """
    commands = []
    with open('proxy_list.txt') as f:
        for line in f:
            commands.append(line)
    return commands


def get_driver():
    """
    Summary get_driver.

    Defines the driver that is used to dynamically load web pages using Chrome.

    Returns
    -------
    driver : chromedriver
        Driver that is used to dynamically load web pages.

    """
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.add_argument('user-agent=%s'%UserAgent().random)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver


def mouse_click(driver, var_two):
    """
    Summary mouse_click.

    Executes randomly chosen mouse clicks to simulate human interaction on the YouTube video.

    Parameters
    ----------
    driver : chromedriver
        Driver that is used to dynamically load web pages.
    var_two : int
        Randomly chosen int between the range of 2 and 5 that determines the number of duplicate tabs that are opened.

    Returns
    -------
    None.

    """
    non_theater_type = ['like', 'dislike', 'subtitles', 'settings', 'random_click_1', 'random_click_2', 'random_click_3', 'volume', 'play',
                        'share', 'save', 'info', 'subscribe']
    clicks_non_theater = {'like':[round(random.uniform(711,735), 2),round(random.uniform(887,909), 2)],
                          'dislike':[round(random.uniform(804,827), 2),round(random.uniform(884,909), 2)],
                          'subtitles':[round(random.uniform(793,825), 2),round(random.uniform(764,785), 2)],
                          'settings':[round(random.uniform(853,873), 2), round(random.uniform(763,790), 2)],
                          'random_click_1':[round(random.uniform(200,1050), 2),round(random.uniform(326,726), 2)],
                          'random_click_2':[round(random.uniform(200,1050), 2),round(random.uniform(326,726), 2)],
                          'random_click_3':[round(random.uniform(200,1050), 2),round(random.uniform(326,726), 2)],
                          'volume':[round(random.uniform(334,372), 2),round(random.uniform(762,783), 2)],
                          'play':[round(random.uniform(223,251), 2),round(random.uniform(759,782), 2)],
                          'share':[round(random.uniform(892,993), 2),round(random.uniform(885,911), 2)],
                          'save':[round(random.uniform(1026,1120), 2),round(random.uniform(887,911), 2)],
                          'info':[round(random.uniform(1154,1186), 2),round(random.uniform(894,909), 2)],
                          'subscribe':[round(random.uniform(1047,1194), 2),round(random.uniform(982,1002), 2)]}

    theater_type = ['play', 'captions', 'settings', 'volume', 'random_click_1', 'random_click_2', 'random_click_3']
    clicks_theater = {'play':[round(random.uniform(56,94), 2),round(random.uniform(959,987), 2)],
                      'captions':[round(random.uniform(959,991), 2),round(random.uniform(958,985), 2)],
                      'settings':[round(random.uniform(1014,1046), 2),round(random.uniform(956,988), 2)],
                      'volume':[round(random.uniform(180,206), 2),round(random.uniform(959,984), 2)],
                      'random_click_1':[round(random.uniform(38,1230), 2),round(random.uniform(288,919), 2)],
                      'random_click_2':[round(random.uniform(38,1230), 2),round(random.uniform(288,919), 2)],
                      'random_click_3':[round(random.uniform(38,1230), 2),round(random.uniform(288,919), 2)]}

    var_one = random.randrange(1, 6)
    flag = True
    if random.randrange(1,3) == 1:
        print(f"\n[~] Executing [{str(var_one)}] randomly selected mouse clicks in standard viewing mode\n")
        for i in range(var_one):
            for j in range(var_two-1):
                driver.switch_to.window(driver.window_handles[j])
                if flag:
                    sleep(0.5)
                    pyautogui.click(x=round(random.uniform(730,810), 2),y=round(random.uniform(820,855), 2),clicks=1,interval=round(random.uniform(1,1.5), 2),button="left")
                    pyautogui.click(x=round(random.uniform(950,1075), 2),y=round(random.uniform(933,979), 2),clicks=1,interval=round(random.uniform(0,1), 2),button="left")
                click = random.choice(non_theater_type)
                pyautogui.click(x=clicks_non_theater[click][0],y=clicks_non_theater[click][1],clicks=1,interval=round(random.uniform(0,3), 2),button="left")
            flag = False
    else:
        print(f"\n[~] Executing [{str(var_one)}] randomly selected mouse clicks in theater viewing mode\n")
        for i in range(var_one):
            for j in range(var_two-1):
                driver.switch_to.window(driver.window_handles[j])
                if flag:
                    sleep(0.5)
                    pyautogui.click(x=round(random.uniform(730,810), 2),y=round(random.uniform(820,855), 2),clicks=1,interval=round(random.uniform(1,1.5), 2),button="left")
                    pyautogui.click(x=round(random.uniform(950,1075), 2),y=round(random.uniform(933,979), 2),clicks=1,interval=round(random.uniform(0,1), 2),button="left")
                    pyautogui.click(x=round(random.uniform(958,985), 2),y=round(random.uniform(762,786), 2),clicks=1,interval=round(random.uniform(0,3), 2),button="left")
                click = random.choice(theater_type)
                pyautogui.click(x=clicks_theater[click][0],y=clicks_theater[click][1],clicks=1,interval=round(random.uniform(0,3), 2),button="left")
            flag = False


def open_tab(driver, query, tab):
    """
    Summary open_tab.

    Opens a tab that contains the desired YouTube video.

    Parameters
    ----------
    driver : chromedriver
        Driver that is used to dynamically load web pages.
    query : str
        Contains the URL that holds the address of the desired YouTube video.
    tab : str
        Tells the driver which tab to switch to.

    Returns
    -------
    None.

    """
    driver.execute_script(f"window.open('about:blank', '{tab}');")
    driver.switch_to.window(tab)
    driver.get('https://www.youtube.com/results?search_query=%s'%query)
    pyautogui.click(x=round(random.uniform(185,525), 2),y=round(random.uniform(391,570), 2),interval=1,clicks=1,button="left")


def search_and_click(search_string, sleep_time):
    """
    Summary search_and_click.

    Searches YouTube for the desired video and clicks on the video to begin playing it.

    Parameters
    ----------
    search_string : str
        Name of the desired video.
    sleep_time : int
        Randomly chosen value within the range of the user-entered min/max that determines amount of time to 'watch' video for.

    Returns
    -------
    None.

    """
    driver = get_driver()
    var_two = random.randrange(3, 6)
    print(f"\n[~] Opening [{str(var_two-1)}] tabs\n")
    query = search_string_to_query(search_string)
    try:
        driver.get('https://www.youtube.com/results?search_query=%s'%query)
        pyautogui.click(x=round(random.uniform(185,525), 2),y=round(random.uniform(391,570), 2),interval=1,clicks=1,button="left")
        for i in range(2, var_two):
            open_tab(driver, query, 'tab'+str(i))
    
        mouse_click(driver, var_two)
        print(f"\n[~] Sleeping for [{sleep_time}] seconds\n")
        sleep(sleep_time)
        driver.quit()
    except:
        driver.quit()


def search_string_to_query(search_string):
    """
    Summary search_string_to_query.

    Converts the name of the desired video into a browser-searchable query.

    Parameters
    ----------
    search_string : str
        Name of the desired video.

    Returns
    -------
    query : str
        Contains the URL that holds the address of the desired YouTube video.

    """
    search = search_string.split(' ')
    query = '+'.join(search)
    return query


def warn(*args, **kwargs):
    """
    Summary warn.

    Suppresses warnings.

    Parameters
    ----------
    *args : iterable
        Iterable object containing args.
    **kwargs : iterable
        Iterable object containing key-word args.

    Returns
    -------
    None.

    """
    pass


def main():
    """
    Summary main.

    Executes the program by calling all of the relevant functions.

    Returns
    -------
    None.

    """
    warnings.warn = warn
    freeze_support()
    args = establish_args()
    search_string = args.search_string
    num_runs = int(args.num_runs)
    min_time = int(args.min)
    max_time = int(args.max)
    commands = get_commands()
    print(f"\n[~] Beginning iteration [1] of [{str(num_runs)}]\n")
    print("\n[~] Please ignore [WDM] messages\n")
    num_failed = 0
    for i in range(num_runs):
        try:
            establish_proxy(commands)
            sleep_time = random.randrange(min_time,max_time)
            search_and_click(search_string, sleep_time)
            if i <  (num_runs - 1):
                print(f"\n[~] Iteration [{str(i+1)}] of [{str(num_runs)}] complete. Beginning next iteration ...\n")
            else:
                print(f"\n[~] Iteration [{str(i+1)}] of [{str(num_runs)}] complete\n")
        except:
            print("\n[~] Failed to establish connection. Moving to next iteration ...\n")
            num_failed += 1
            continue
    print(f"\n[~] [{str(num_failed)}] iterations failed due to failed connection")

if __name__ == "__main__":
        main()