# 妙語說書人 模擬器 團康桌遊小幫手

> 2021 LineBot 實作
> 截止：2022/1/2

## 引言

桌遊是不少大學生在課業繁忙之餘，又在避免手機遊戲成癮情況下，經常有的娛樂。除了能讓學生們在忙裡偷閒，能增進同學們之間的友誼，與四年的同窗聯絡感情。
然而，桌遊可不是晃雃就玩，日常裡多得是想玩桌遊卻不姓身邊沒有人想到要帶桌遊的情況。
這時，這款模擬火紅桌遊「妙語說書人」的聊天機器人，就能派上用場啦。
不僅不用自己帶體積龐大的桌遊套組，這款Ｂ還能代替你做出洗牌、發牌、抽排、翻牌的功能。
有了這款機器人，再也不用怕想玩桌遊時沒東西可以玩了！

## 遊戲介紹

「妙語說書人」這款遊戲是在考驗玩家的文學造詣，聽故事的人，要能揣摩說故事的人的心境與想法，說故事的人，則要能在平鋪直述與曲折隱晦之間找到平衡點。故事每一輪各玩家手中皆有五張卡牌，每張卡牌上都有一幀天馬行空的畫作。每個人都會輪流當說書人，當到說書人的人要從自己手中選出一張牌（先蓋起），並且根據這張牌的圖畫想出一個句子，說出句子後，其他聽書的人便要根據該句子從自己手中找到一張最相似的卡牌（混淆視聽用），接著聽書人會將所有人出的卡牌，包括他自己的收集起來洗牌，最後翻開來讓大家猜測哪張才是說書人出的牌。

## 計分規則

倘若沒有人猜中或所有人都猜對，就代表說書人的句子太過直白或太過隱晦，沒有拿捏好文學性的分寸，此時說書人拿不到任何分數，其他人則可以各得二分。
以上的情況之外，猜對者可以同說書人得三分。
另外，聽書人若成功誤導別人，讓他人投自己，則每票各加一分。

最先到達30分者獲得勝利。


# LineBot 2021
## 以下為作業ReadMe範本
[![Maintainability](https://api.codeclimate.com/v1/badges/dc7fa47fcd809b99d087/maintainability)](https://codeclimate.com/github/NCKU-CCS/TOC-Project-2020/maintainability)

[![Known Vulnerabilities](https://snyk.io/test/github/NCKU-CCS/TOC-Project-2020/badge.svg)](https://snyk.io/test/github/NCKU-CCS/TOC-Project-2020)

Template Code for TOC Project 2020

A Line bot based on a finite state machine

More details in the [Slides](https://hackmd.io/@TTW/ToC-2019-Project#) and [FAQ](https://hackmd.io/s/B1Xw7E8kN)

## Setup

### Prerequisite
* Python 3.6
* Pipenv
* Facebook Page and App
* HTTPS Server

#### Install Dependency
```sh
pip3 install pipenv

pipenv --three

pipenv install

pipenv shell
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)
	* [Note: macOS Install error](https://github.com/pygraphviz/pygraphviz/issues/100)


#### Secret Data
You should generate a `.env` file to set Environment Variables refer to our `.env.sample`.
`LINE_CHANNEL_SECRET` and `LINE_CHANNEL_ACCESS_TOKEN` **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

#### a. Ngrok installation
* [ macOS, Windows, Linux](https://ngrok.com/download)

or you can use Homebrew (MAC)
```sh
brew cask install ngrok
```

**`ngrok` would be used in the following instruction**

```sh
ngrok http 8000
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python3 app.py
```

#### b. Servo

Or You can use [servo](http://serveo.net/) to expose local servers to the internet.


## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "go to state1"
		* Reply: "I'm entering state1"

	* Input: "go to state2"
		* Reply: "I'm entering state2"

## Deploy
Setting to deploy webhooks on Heroku.

### Heroku CLI installation

* [macOS, Windows](https://devcenter.heroku.com/articles/heroku-cli)

or you can use Homebrew (MAC)
```sh
brew tap heroku/brew && brew install heroku
```

or you can use Snap (Ubuntu 16+)
```sh
sudo snap install --classic heroku
```

### Connect to Heroku

1. Register Heroku: https://signup.heroku.com

2. Create Heroku project from website

3. CLI Login

	`heroku login`

### Upload project to Heroku

1. Add local project to Heroku project

	heroku git:remote -a {HEROKU_APP_NAME}

2. Upload project

	```
	git add .
	git commit -m "Add code"
	git push -f heroku master
	```

3. Set Environment - Line Messaging API Secret Keys

	```
	heroku config:set LINE_CHANNEL_SECRET=your_line_channel_secret
	heroku config:set LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
	```

4. Your Project is now running on Heroku!

	url: `{HEROKU_APP_NAME}.herokuapp.com/callback`

	debug command: `heroku logs --tail --app {HEROKU_APP_NAME}`

5. If fail with `pygraphviz` install errors

	run commands below can solve the problems
	```
	heroku buildpacks:set heroku/python
	heroku buildpacks:add --index 1 heroku-community/apt
	```

	refference: https://hackmd.io/@ccw/B1Xw7E8kN?type=view#Q2-如何在-Heroku-使用-pygraphviz

## Reference
[Pipenv](https://medium.com/@chihsuan/pipenv-更簡單-更快速的-python-套件管理工具-135a47e504f4) ❤️ [@chihsuan](https://github.com/chihsuan)

[TOC-Project-2019](https://github.com/winonecheng/TOC-Project-2019) ❤️ [@winonecheng](https://github.com/winonecheng)

Flask Architecture ❤️ [@Sirius207](https://github.com/Sirius207)

[Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)
