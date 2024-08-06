import Image from "next/image";
import logo from "@/public/image-removebg-preview (11).png";
import { RegLogStyle } from "@/Style";
import { ResetPasswordForm } from "@/Page-Components/Form";
import Link from "next/link";

export default function page() {
    return (
        <div className={`${RegLogStyle.center} flex-col mt-10`}>
            <div className={`${RegLogStyle.center} flex-col`}>
                <Link href="/">
                    <Image
                        src={logo}
                        alt="Visual Subject Learning"
                        width={60}
                        priority
                    />
                </Link>
                <h1 className="font-header1 text-md_pl mt-10">
                    Đặt lại mật khẩu
                </h1>
            </div>

            <div
                className="flex flex-col gap-6 mt-10 w-[500px] rounded-card shadow-[5px_5px_10px_rgba(0,0,0,0.3)] pb-[25px] pt-[22.5px] px-[37px] 
                bg-muted"
            >
                <ResetPasswordForm />
            </div>
        </div>
    );
}
