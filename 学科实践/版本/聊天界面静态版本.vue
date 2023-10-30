<template>
  <view class="container">
    <view class="chat-body">
      <view class="chat-one">
        <image class="chat-face" src="/static/faces/1.png" />
        <view class="chat-box">
          <view class="chat-sender">小姐姐</view>
          <view class="chat-content">你好，我是小姐姐!</view>
        </view>
      </view>
      <view class="chat-one">
        <image class="chat-face" src="@/static/faces/1.png" />
        <view class="chat-box">
          <view class="chat-sender">小姐姐</view>
          <image class="chat-img" src="/static/imgs/1.png" mode="widthFix"></image>
        </view>
      </view>
      <view class="chat-one chat-one-mine">
        <view class="chat-box">
          <view class="chat-content">哇，小姐姐好美啊!</view>
        </view>
        <image class="chat-face" src="/static/faces/2.png" />
      </view>
      <view class="chat-one chat-one-mine">
        <view class="chat-box">
          <image class="chat-img" src="/static/imgs/2.png" mode="widthFix"></image>
        </view>
        <image class="chat-face" src="/static/faces/2.png" />
      </view>
    </view>
    <!-- 聊天输入 -->
    <view class="chat-footer">
      <input class="msg-input" type="text" cursor-spacing="16" />
      <!-- <image class="img-chose" src="@/static/img.png" /> -->
      <view class="send-btn">发送</view>
    </view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      title: 'Hello'
    }
  },
  onLoad() {

  },
  methods: {

  }
}
</script>





