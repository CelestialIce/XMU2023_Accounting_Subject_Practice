<script>
	export default {
		onLaunch: function() {
			console.log('App Launch')
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		}
	}
</script>

<style>
	.container {
	  background-color: #f1f1f1;
	  min-height: 100vh;
	}
	
	.container .chat-body {
	  padding-bottom: 178upx;
	}
	
	.container .chat-body .chat-one {
	  display: flex;
	  flex-wrap: wrap;
	  justify-content: flex-start;
	  align-items: flex-start;
	  padding: 20upx 0;
	}
	
	.container .chat-body .chat-one .chat-face {
	  width: 84upx;
	  height: 84upx;
	  border-radius: 10upx;
	  margin-left: 40upx;
	}
	
	.container .chat-body .chat-one .chat-box {
	  max-width: calc(100% - 290upx);
	  margin-left: 20upx;
	  font-size: 30upx;
	}
	
	.container .chat-body .chat-one .chat-sender {
	  color: #888;
	  font-size: 28upx;
	  margin-top: -8upx;
	  margin-bottom: 10upx;
	}
	
	.container .chat-body .chat-one .chat-content {
	  background-color: #fff;
	  border-radius: 5px;
	  padding: 10px;
	}
	
	.container .chat-body .chat-one .chat-img {
	  float: left;
	  max-width: 60%;
	  border-radius: 5px;
	}
	
	.container .chat-body .chat-one.chat-one-mine {
	  justify-content: flex-end;
	}
	
	.container .chat-body .chat-one.chat-one-mine .chat-face {
	  margin-left: 0;
	  margin-right: 40upx;
	}
	
	.container .chat-body .chat-one.chat-one-mine .chat-box {
	  margin-right: 20upx;
	}
	
	.container .chat-body .chat-one.chat-one-mine .chat-img {
	  float: right;
	}
	
.container .chat-footer {
  width: 100%; /* 横向铺满整个底部 */
  height: 120upx; /* 调整高度，根据需要调整 */
  position: fixed;
  bottom: 0;
  left: 0;
  background-color: #f1f1f1;
  display: flex;
  flex-direction: row;
  justify-content: space-between; /* 控件之间分开 */
  align-items: center;
  border-top: 1upx solid #ddd;
  padding: 0 20upx; /* 适当减小左右内边距 */
}

.container .chat-footer .msg-input {
  background-color: #fff;
  flex: 1; /* 让输入框占据剩余空间 */
  height: 70upx;
  line-height: 70upx;
  font-size: 30upx;
  border-radius: 10upx;
  padding: 0 20upx;
  margin-right: 20upx; /* 添加右侧间距 */
}

.container .img-chose {
  height: 70upx;
  width: 70upx;
  margin-right: 20upx; /* 添加右侧间距 */
}

.container .chat-footer .send-btn {
  height: 40upx;
  width: 120upx;
}

</style>
