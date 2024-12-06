import kue from 'kue';


const queue = kue.createQueue()
const job = queue.create('push_notification_code', {
    phoneNumber: "911156895",
    message: "messaging you"
}).save((err) => {
    if (err) {
        console.log('Notification job failed');
        
    } else {
        console.log(`Notification job created: ${job.id}`);
    }
})

job.on('complete', () => {
    console.log('Notification job failed');
})
