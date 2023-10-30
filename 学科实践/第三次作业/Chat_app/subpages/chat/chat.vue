<template>
	<view class="container">
		<view class="chat-body">
		  <view v-for="(item, index) in chatList" :key="index">
		    <view class="chat-one" v-if="!item.isMe">
		      <image class="chat-face" src="@/static/faces/1.png" />
		      <view class="chat-box">
		        <view class="chat-sender">小姐姐</view>
		        <view class="chat-content" v-if="item.type === 'txt'">{{ item.content }}</view>
		        <image class="chat-img" v-if="item.type === 'img'" :src="item.content" mode="widthFix" />
		      </view>
		    </view>
		    <view v-else class="chat-one chat-one-mine">
		      <view class="chat-box">
		        <view class="chat-content" v-if="item.type === 'txt'">{{ item.content }}</view>
		        <image class="chat-img" v-if="item.type === 'img'" :src="item.content" mode="widthFix"></image>
		      </view>
		      <image class="chat-face" src="@/static/faces/2.png" />
		    </view>
		  </view>
		</view>
		<view class="chat-footer">
		  <input class="msg-input" type="text" v-model="myInput" @keydown.enter="sendMsg" />
		  <image class="img-chose" src="@/static/tabbar-icons/img.png" @click="chooseImgAndSend" />
		  <view class="send-btn" @click="sendMsg">发送</view>
		</view>
	</view>
  
</template>

<script>
export default {
  data() {
    return {
      chatList: [
        {
          isMe: false,
          type: 'txt',
          content: '你好，我是小姐姐！'
        },
        {
          isMe: false,
          type: 'img',
          content: '/static/imgs/1.png'
        },
        {
          isMe: true,
          type: 'txt',
          content: '哇，小姐姐好美啊！'
        },
        {
          isMe: true,
          type: 'img',
          content: '/static/imgs/2.png'
        }
      ],
      myInput: ''
    };
  },
  onShow() {
    if (uni.getStorageSync('chatList')) {
      this.chatList = JSON.parse(uni.getStorageSync('chatList'));
    }
  },
  methods: {
    sendMsg() {
      if (!this.myInput) return;
      let txtMsg = {
        isMe: true,
        type: 'txt',
        content: this.myInput
      };
      this.chatList.push(txtMsg);
      uni.setStorageSync('chatList', JSON.stringify(this.chatList));
      this.myInput = '';
	  this.scrollToBottom(); // 滚动到底部
    },
    chooseImgAndSend() {
      uni.chooseImage({
        count: 1,
        sizeType: ['original', 'compressed'],
        sourceType: ['album', 'camera'],
        success: (res) => {
          console.log(res.tempFilePaths[0]);
          let sendMsg = {
            isMe: true,
            type: 'img',
            content: res.tempFilePaths[0]
          };
          this.chatList.push(sendMsg);
          let resMsg = {
            isMe: false,
            type: 'img',
            content: res.tempFilePaths[0]
          };
          // this.chatList.push(resMsg);
          uni.pageScrollTo({
            scrollTop: 999999,
            duration: 0
          });
          uni.setStorageSync('chatList', JSON.stringify(this.chatList));
		  this.scrollToBottom(); // 滚动到底部
        }
      });
    },
	  scrollToBottom() {
	    // 滚动到底部
	    uni.createSelectorQuery()
	      .select('.container') // 选择聊天内容容器的类名
	      .boundingClientRect(rect => {
	        uni.pageScrollTo({
	          scrollTop: rect.height+100000
	        });
	      })
	      .exec();
	  }
	
	
  }
};

</script>

