import styles from './SubmitButton.module.css'

function SubmitButton({text}) {
    return (
        <div>
            <button className={styles.submitbtn}>{text}</button>
        </div>
    )
}

export default SubmitButton