from flask import render_template, send_file


def get_user_img_url():
    img_url=[
        'bili_level_distribution.png',
        'bili_role_distribution.png',
        'uploader_distribution.png',
    ]
    #返回这三个图片的url
    return img_url


def get_user_heat_map_url():
    img_url=[
        'influence_update_cycle_correlation.jpg.png',
    ]

    return img_url